<div class="section" id="module-pulumi_aws.cloudhsmv2">
<span id="cloudhsmv2"></span><h1>cloudhsmv2<a class="headerlink" href="#module-pulumi_aws.cloudhsmv2" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cloudhsmv2.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudhsmv2.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>hsm_type=None</em>, <em>source_backup_identifier=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudHSM v2 cluster.</p>
<p>For information about CloudHSM v2, see the
[AWS CloudHSM User Guide][1] and the [Amazon
CloudHSM API Reference][2].</p>
<blockquote>
<div><strong>NOTE:</strong> CloudHSM can take up to several minutes to be set up.
Practically no single attribute can be updated except TAGS.
If you need to delete a cluster, you have to remove its HSM modules first.
To initialize cluster you have to sign CSR and upload it.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>hsm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of HSM module in the cluster. Currently, only hsm1.medium is supported.</li>
<li><strong>source_backup_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of Cloud HSM v2 cluster backup to be restored.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of subnets in which cluster will operate.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_certificates">
<code class="descname">cluster_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cluster certificates.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_certificate</span></code> - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster’s owner.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_csr</span></code> - The certificate signing request (CSR). Available only in UNINITIALIZED state.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.aws_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by AWS CloudHSM.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.hsm_certificate</span></code> - The HSM certificate issued (signed) by the HSM hardware.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.manufacturer_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by the hardware manufacturer.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_id">
<code class="descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the CloudHSM cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.cluster_state">
<code class="descname">cluster_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.cluster_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.hsm_type">
<code class="descname">hsm_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.hsm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of HSM module in the cluster. Currently, only hsm1.medium is supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group associated with the CloudHSM cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.source_backup_identifier">
<code class="descname">source_backup_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.source_backup_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of Cloud HSM v2 cluster backup to be restored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of subnets in which cluster will operate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Cluster.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that the CloudHSM cluster resides in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudhsmv2.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudhsmv2.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>cluster_certificates=None</em>, <em>cluster_id=None</em>, <em>cluster_state=None</em>, <em>security_group_id=None</em>, <em>subnet_ids=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.cluster_certificates">
<code class="descname">cluster_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.cluster_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cluster certificates.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_certificate</span></code> - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster’s owner.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.cluster_csr</span></code> - The certificate signing request (CSR). Available only in UNINITIALIZED state.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.aws_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by AWS CloudHSM.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.hsm_certificate</span></code> - The HSM certificate issued (signed) by the HSM hardware.</li>
<li><code class="docutils literal notranslate"><span class="pre">cluster_certificates.0.manufacturer_hardware_certificate</span></code> - The HSM hardware certificate issued (signed) by the hardware manufacturer.
The number of available cluster certificates may vary depending on state of the cluster.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group associated with the CloudHSM cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of subnets in which cluster operates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that the CloudHSM cluster resides in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudhsmv2.Hsm">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudhsmv2.</code><code class="descname">Hsm</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>cluster_id=None</em>, <em>ip_address=None</em>, <em>subnet_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an HSM module in Amazon CloudHSM v2 cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.</li>
<li><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of Cloud HSM v2 cluster to which HSM will be added.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of HSM module. Must be within the CIDR of selected subnet.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of subnet in which HSM module will be located.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.cluster_id">
<code class="descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of Cloud HSM v2 cluster to which HSM will be added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_eni_id">
<code class="descname">hsm_eni_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_eni_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the ENI interface allocated for HSM module.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_id">
<code class="descname">hsm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the HSM module.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.hsm_state">
<code class="descname">hsm_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.hsm_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the HSM module.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of HSM module. Must be within the CIDR of selected subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudhsmv2.Hsm.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of subnet in which HSM module will be located.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudhsmv2.Hsm.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudhsmv2.Hsm.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.Hsm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.cloudhsmv2.get_cluster">
<code class="descclassname">pulumi_aws.cloudhsmv2.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>cluster_id=None</em>, <em>cluster_state=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudhsmv2.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a CloudHSM v2 cluster</p>
</dd></dl>

</div>
