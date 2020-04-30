---
title: Module cloudhsmv2
title_tag: Module cloudhsmv2 | Package pulumi_aws | Python SDK
linktitle: cloudhsmv2
notitle: true
---

<div class="section" id="cloudhsmv2">
<h1>cloudhsmv2<a class="headerlink" href="#cloudhsmv2" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudhsmv2"></span><dl class="py class">
<dt id="pulumi_aws.cloudhsmv2.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudhsmv2.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudhsmv2.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudhsmv2.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hsm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_backup_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudHSM v2 cluster.</p>
<p>For information about CloudHSM v2, see the
<a class="reference external" href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html">AWS CloudHSM User Guide</a> and the [Amazon
CloudHSM API Reference][2].</p>
<blockquote>
<div><p><strong>NOTE:</strong> CloudHSM can take up to several minutes to be set up.
Practically no single attribute can be updated except TAGS.
If you need to delete a cluster, you have to remove its HSM modules first.
To initialize cluster, you have to add an hsm instance to the cluster then sign CSR and upload it.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hsm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of HSM module in the cluster. Currently, only hsm1.medium is supported.</p></li>
<li><p><strong>source_backup_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of Cloud HSM v2 cluster backup to be restored.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of subnets in which cluster will operate.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_certificates">
<code class="sig-name descname">cluster_certificates</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cluster certificates.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_certificate</span></code> - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster’s owner.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_csr</span></code> - The certificate signing request (CSR). Available only in UNINITIALIZED state after an hsm instance is added to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.aws_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by AWS CloudHSM.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.hsm_certificate</span></code> - The HSM certificate issued (signed) by the HSM hardware.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.manufacturer_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by the hardware manufacturer.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">awsHardwareCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCsr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hsmCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manufacturerHardwareCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the CloudHSM cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_state">
<code class="sig-name descname">cluster_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.hsm_type">
<code class="sig-name descname">hsm_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.hsm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of HSM module in the cluster. Currently, only hsm1.medium is supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group associated with the CloudHSM cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.source_backup_identifier">
<code class="sig-name descname">source_backup_identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.source_backup_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of Cloud HSM v2 cluster backup to be restored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of subnets in which cluster will operate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that the CloudHSM cluster resides in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudhsmv2.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hsm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_backup_identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of cluster certificates.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_certificates.0.cluster_certificate` - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster&#39;s owner.
* `cluster_certificates.0.cluster_csr` - The certificate signing request (CSR). Available only in UNINITIALIZED state after an hsm instance is added to the cluster.
* `cluster_certificates.0.aws_hardware_certificate` - The HSM hardware certificate issued (signed) by AWS CloudHSM.
* `cluster_certificates.0.hsm_certificate` - The HSM certificate issued (signed) by the HSM hardware.
* `cluster_certificates.0.manufacturer_hardware_certificate` - The HSM hardware certificate issued (signed) by the hardware manufacturer.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the CloudHSM cluster.</p></li>
<li><p><strong>cluster_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the cluster.</p></li>
<li><p><strong>hsm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of HSM module in the cluster. Currently, only hsm1.medium is supported.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group associated with the CloudHSM cluster.</p></li>
<li><p><strong>source_backup_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of Cloud HSM v2 cluster backup to be restored.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of subnets in which cluster will operate.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that the CloudHSM cluster resides in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">awsHardwareCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCsr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hsmCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manufacturerHardwareCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudhsmv2.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudhsmv2.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.cluster_certificates">
<code class="sig-name descname">cluster_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.cluster_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cluster certificates.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_certificate</span></code> - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster’s owner.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_csr</span></code> - The certificate signing request (CSR). Available only in UNINITIALIZED state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.aws_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by AWS CloudHSM.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.hsm_certificate</span></code> - The HSM certificate issued (signed) by the HSM hardware.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.manufacturer_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by the hardware manufacturer.
The number of available cluster certificates may vary depending on state of the cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group associated with the CloudHSM cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of subnets in which cluster operates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that the CloudHSM cluster resides in.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudhsmv2.Hsm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudhsmv2.</code><code class="sig-name descname">Hsm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an HSM module in Amazon CloudHSM v2 cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of Cloud HSM v2 cluster to which HSM will be added.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of HSM module. Must be within the CIDR of selected subnet.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of subnet in which HSM module will be located.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of Cloud HSM v2 cluster to which HSM will be added.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_eni_id">
<code class="sig-name descname">hsm_eni_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_eni_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the ENI interface allocated for HSM module.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_id">
<code class="sig-name descname">hsm_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the HSM module.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_state">
<code class="sig-name descname">hsm_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the HSM module.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of HSM module. Must be within the CIDR of selected subnet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of subnet in which HSM module will be located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudhsmv2.Hsm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hsm_eni_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hsm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hsm_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hsm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of Cloud HSM v2 cluster to which HSM will be added.</p></li>
<li><p><strong>hsm_eni_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the ENI interface allocated for HSM module.</p></li>
<li><p><strong>hsm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the HSM module.</p></li>
<li><p><strong>hsm_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the HSM module.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of HSM module. Must be within the CIDR of selected subnet.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of subnet in which HSM module will be located.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudhsmv2.Hsm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.Hsm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.cloudhsmv2.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a CloudHSM v2 cluster</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_id</strong> (<em>str</em>) – The id of Cloud HSM v2 cluster.</p></li>
<li><p><strong>cluster_state</strong> (<em>str</em>) – The state of the cluster to be found.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
