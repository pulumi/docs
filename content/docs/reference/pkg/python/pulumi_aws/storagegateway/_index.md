---
title: Module storagegateway
linktitle: storagegateway
notitle: true
---

<div class="section" id="storagegateway">
<h1>storagegateway<a class="headerlink" href="#storagegateway" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.storagegateway"></span><dl class="class">
<dt id="pulumi_aws.storagegateway.AwaitableGetLocalDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">AwaitableGetLocalDiskResult</code><span class="sig-paren">(</span><em class="sig-param">disk_id=None</em>, <em class="sig-param">disk_node=None</em>, <em class="sig-param">disk_path=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.AwaitableGetLocalDiskResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.storagegateway.Cache">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">Cache</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway cache.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Storage Gateway API provides no method to remove a cache disk. Destroying this resource does not perform any Storage Gateway actions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Cache.disk_id">
<code class="sig-name descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Cache.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Cache.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cache resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Cache.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Cache.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">CachesIscsiVolume</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">source_volume_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_name=None</em>, <em class="sig-param">volume_size_in_bytes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway cached iSCSI volume.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The gateway must have cache added (e.g. via the <cite>``storagegateway.Cache`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html">https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html</a>&gt;`_ resource) before creating volumes otherwise the Storage Gateway API will return an error.</p>
<p><strong>NOTE:</strong> The gateway must have an upload buffer added (e.g. via the <cite>``storagegateway.UploadBuffer`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/storagegateway_upload_buffer.html">https://www.terraform.io/docs/providers/aws/r/storagegateway_upload_buffer.html</a>&gt;`_ resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as <code class="docutils literal notranslate"><span class="pre">UPLOAD</span> <span class="pre">BUFFER</span> <span class="pre">NOT</span> <span class="pre">CONFIGURED</span></code>.</p>
</div></blockquote>
<blockquote>
<div><p><strong>NOTE:</strong> These examples are referencing the <cite>``storagegateway.Cache`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html">https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html</a>&gt;`_ resource <code class="docutils literal notranslate"><span class="pre">gateway_arn</span></code> attribute to ensure this provider properly adds cache before creating the volume. If you are not using this method, you may need to declare an expicit dependency (e.g. via <code class="docutils literal notranslate"><span class="pre">depends_on</span> <span class="pre">=</span> <span class="pre">[&quot;aws_storagegateway_cache.example&quot;]</span></code>) to ensure proper ordering.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID of the snapshot to restore as the new cached volume. e.g. <code class="docutils literal notranslate"><span class="pre">snap-1122aabb</span></code>.</p></li>
<li><p><strong>source_volume_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume’s latest recovery point. The <code class="docutils literal notranslate"><span class="pre">volume_size_in_bytes</span></code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>target_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.</p></li>
<li><p><strong>volume_size_in_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume in bytes.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.chap_enabled">
<code class="sig-name descname">chap_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.chap_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether mutual CHAP is enabled for the iSCSI target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.lun_number">
<code class="sig-name descname">lun_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.lun_number" title="Permalink to this definition">¶</a></dt>
<dd><p>Logical disk number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_port">
<code class="sig-name descname">network_interface_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used to communicate with iSCSI targets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID of the snapshot to restore as the new cached volume. e.g. <code class="docutils literal notranslate"><span class="pre">snap-1122aabb</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.source_volume_arn">
<code class="sig-name descname">source_volume_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.source_volume_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume’s latest recovery point. The <code class="docutils literal notranslate"><span class="pre">volume_size_in_bytes</span></code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.target_arn">
<code class="sig-name descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Target Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.target_name">
<code class="sig-name descname">target_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.target_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_arn">
<code class="sig-name descname">volume_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_id">
<code class="sig-name descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume ID, e.g. <code class="docutils literal notranslate"><span class="pre">vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_size_in_bytes">
<code class="sig-name descname">volume_size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume in bytes.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">chap_enabled=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">lun_number=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">network_interface_port=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">source_volume_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_arn=None</em>, <em class="sig-param">target_name=None</em>, <em class="sig-param">volume_arn=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_size_in_bytes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CachesIscsiVolume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p></li>
<li><p><strong>chap_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether mutual CHAP is enabled for the iSCSI target.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
<li><p><strong>lun_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logical disk number.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.</p></li>
<li><p><strong>network_interface_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used to communicate with iSCSI targets.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID of the snapshot to restore as the new cached volume. e.g. <code class="docutils literal notranslate"><span class="pre">snap-1122aabb</span></code>.</p></li>
<li><p><strong>source_volume_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume’s latest recovery point. The <code class="docutils literal notranslate"><span class="pre">volume_size_in_bytes</span></code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName</span></code>.</p></li>
<li><p><strong>target_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.</p></li>
<li><p><strong>volume_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Volume ID, e.g. <code class="docutils literal notranslate"><span class="pre">vol-12345678</span></code>.</p></li>
<li><p><strong>volume_size_in_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume in bytes.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Gateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">Gateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_key=None</em>, <em class="sig-param">gateway_ip_address=None</em>, <em class="sig-param">gateway_name=None</em>, <em class="sig-param">gateway_timezone=None</em>, <em class="sig-param">gateway_type=None</em>, <em class="sig-param">medium_changer_type=None</em>, <em class="sig-param">smb_active_directory_settings=None</em>, <em class="sig-param">smb_guest_password=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tape_drive_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.</p>
<blockquote>
<div><p>NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving <code class="docutils literal notranslate"><span class="pre">The</span> <span class="pre">specified</span> <span class="pre">gateway</span> <span class="pre">is</span> <span class="pre">not</span> <span class="pre">connected</span></code> errors during resource creation (gateway activation), ensure your gateway instance meets the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html">Storage Gateway requirements</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">gateway_ip_address</span></code>. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p></li>
<li><p><strong>gateway_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Gateway IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</p></li>
<li><p><strong>gateway_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the gateway.</p></li>
<li><p><strong>gateway_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time zone for the gateway. The time zone is of the format “GMT”, “GMT-hr:mm”, or “GMT+hr:mm”. For example, <code class="docutils literal notranslate"><span class="pre">GMT-4:00</span></code> indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway’s maintenance schedule.</p></li>
<li><p><strong>gateway_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the gateway. The default value is <code class="docutils literal notranslate"><span class="pre">STORED</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">CACHED</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code>, <code class="docutils literal notranslate"><span class="pre">STORED</span></code>, <code class="docutils literal notranslate"><span class="pre">VTL</span></code>.</p></li>
<li><p><strong>smb_active_directory_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code> authentication SMB file shares. More details below.</p></li>
<li><p><strong>smb_guest_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Guest password for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code> authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>tape_drive_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: <code class="docutils literal notranslate"><span class="pre">IBM-ULT3580-TD5</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>smb_active_directory_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the domain that you want the gateway to join.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the user who has permission to add the gateway to the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name of user who has permission to add the gateway to the Active Directory domain.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.activation_key">
<code class="sig-name descname">activation_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.activation_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">gateway_ip_address</span></code>. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_id">
<code class="sig-name descname">gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_ip_address">
<code class="sig-name descname">gateway_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_name">
<code class="sig-name descname">gateway_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_timezone">
<code class="sig-name descname">gateway_timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Time zone for the gateway. The time zone is of the format “GMT”, “GMT-hr:mm”, or “GMT+hr:mm”. For example, <code class="docutils literal notranslate"><span class="pre">GMT-4:00</span></code> indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway’s maintenance schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_type">
<code class="sig-name descname">gateway_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the gateway. The default value is <code class="docutils literal notranslate"><span class="pre">STORED</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">CACHED</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code>, <code class="docutils literal notranslate"><span class="pre">STORED</span></code>, <code class="docutils literal notranslate"><span class="pre">VTL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.smb_active_directory_settings">
<code class="sig-name descname">smb_active_directory_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.smb_active_directory_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code> authentication SMB file shares. More details below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the domain that you want the gateway to join.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password of the user who has permission to add the gateway to the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user name of user who has permission to add the gateway to the Active Directory domain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.smb_guest_password">
<code class="sig-name descname">smb_guest_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.smb_guest_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Guest password for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code> authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.tape_drive_type">
<code class="sig-name descname">tape_drive_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.tape_drive_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: <code class="docutils literal notranslate"><span class="pre">IBM-ULT3580-TD5</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Gateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_key=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">gateway_id=None</em>, <em class="sig-param">gateway_ip_address=None</em>, <em class="sig-param">gateway_name=None</em>, <em class="sig-param">gateway_timezone=None</em>, <em class="sig-param">gateway_type=None</em>, <em class="sig-param">medium_changer_type=None</em>, <em class="sig-param">smb_active_directory_settings=None</em>, <em class="sig-param">smb_guest_password=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tape_drive_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Gateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Gateway activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">gateway_ip_address</span></code>. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the gateway.</p></li>
<li><p><strong>gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the gateway.</p></li>
<li><p><strong>gateway_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Gateway IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</p></li>
<li><p><strong>gateway_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the gateway.</p></li>
<li><p><strong>gateway_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time zone for the gateway. The time zone is of the format “GMT”, “GMT-hr:mm”, or “GMT+hr:mm”. For example, <code class="docutils literal notranslate"><span class="pre">GMT-4:00</span></code> indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway’s maintenance schedule.</p></li>
<li><p><strong>gateway_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the gateway. The default value is <code class="docutils literal notranslate"><span class="pre">STORED</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">CACHED</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code>, <code class="docutils literal notranslate"><span class="pre">STORED</span></code>, <code class="docutils literal notranslate"><span class="pre">VTL</span></code>.</p></li>
<li><p><strong>smb_active_directory_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code> authentication SMB file shares. More details below.</p></li>
<li><p><strong>smb_guest_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Guest password for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code> authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>tape_drive_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: <code class="docutils literal notranslate"><span class="pre">IBM-ULT3580-TD5</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>smb_active_directory_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the domain that you want the gateway to join.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the user who has permission to add the gateway to the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name of user who has permission to add the gateway to the Active Directory domain.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Gateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Gateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">GetLocalDiskResult</code><span class="sig-paren">(</span><em class="sig-param">disk_id=None</em>, <em class="sig-param">disk_node=None</em>, <em class="sig-param">disk_path=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocalDisk.</p>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult.disk_id">
<code class="sig-name descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk identifier. e.g. <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.storagegateway.NfsFileShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">NfsFileShare</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_lists=None</em>, <em class="sig-param">default_storage_class=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">guess_mime_type_enabled=None</em>, <em class="sig-param">kms_encrypted=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">location_arn=None</em>, <em class="sig-param">nfs_file_share_defaults=None</em>, <em class="sig-param">object_acl=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">requester_pays=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">squash=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway NFS File Share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to <code class="docutils literal notranslate"><span class="pre">[&quot;0.0.0.0/0&quot;]</span></code> to not limit access. Minimum 1 item. Maximum 100 items.</p></li>
<li><p><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</p></li>
<li><p><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p></li>
<li><p><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</p></li>
<li><p><strong>nfs_file_share_defaults</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with file share default values. More information below.</p></li>
<li><p><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p></li>
<li><p><strong>squash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maps a user to anonymous user. Defaults to <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code> (only root is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">NoSquash</span></code> (no one is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">AllSquash</span></code> (everyone is mapped to anonymous user)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nfs_file_share_defaults</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">directoryMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Unix directory mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0777&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Unix file mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0666&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default group ID for the file share (unless the files have another group ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default owner ID for the file share (unless the files have another owner ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the NFS File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.client_lists">
<code class="sig-name descname">client_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.client_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to <code class="docutils literal notranslate"><span class="pre">[&quot;0.0.0.0/0&quot;]</span></code> to not limit access. Minimum 1 item. Maximum 100 items.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.default_storage_class">
<code class="sig-name descname">default_storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.default_storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.fileshare_id">
<code class="sig-name descname">fileshare_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.fileshare_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the NFS File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the file gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.guess_mime_type_enabled">
<code class="sig-name descname">guess_mime_type_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.guess_mime_type_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.kms_encrypted">
<code class="sig-name descname">kms_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.kms_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.location_arn">
<code class="sig-name descname">location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the backed storage used for storing file data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.nfs_file_share_defaults">
<code class="sig-name descname">nfs_file_share_defaults</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.nfs_file_share_defaults" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument with file share default values. More information below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">directoryMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Unix directory mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0777&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Unix file mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0666&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The default group ID for the file share (unless the files have another group ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The default owner ID for the file share (unless the files have another owner ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.object_acl">
<code class="sig-name descname">object_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.object_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.read_only">
<code class="sig-name descname">read_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.requester_pays">
<code class="sig-name descname">requester_pays</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.requester_pays" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.squash">
<code class="sig-name descname">squash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.squash" title="Permalink to this definition">¶</a></dt>
<dd><p>Maps a user to anonymous user. Defaults to <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code> (only root is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">NoSquash</span></code> (no one is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">AllSquash</span></code> (everyone is mapped to anonymous user)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.NfsFileShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">client_lists=None</em>, <em class="sig-param">default_storage_class=None</em>, <em class="sig-param">fileshare_id=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">guess_mime_type_enabled=None</em>, <em class="sig-param">kms_encrypted=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">location_arn=None</em>, <em class="sig-param">nfs_file_share_defaults=None</em>, <em class="sig-param">object_acl=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">requester_pays=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">squash=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NfsFileShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the NFS File Share.</p></li>
<li><p><strong>client_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to <code class="docutils literal notranslate"><span class="pre">[&quot;0.0.0.0/0&quot;]</span></code> to not limit access. Minimum 1 item. Maximum 100 items.</p></li>
<li><p><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p></li>
<li><p><strong>fileshare_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the NFS File Share.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</p></li>
<li><p><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p></li>
<li><p><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</p></li>
<li><p><strong>nfs_file_share_defaults</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with file share default values. More information below.</p></li>
<li><p><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p></li>
<li><p><strong>squash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maps a user to anonymous user. Defaults to <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code> (only root is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">NoSquash</span></code> (no one is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">AllSquash</span></code> (everyone is mapped to anonymous user)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nfs_file_share_defaults</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">directoryMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Unix directory mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0777&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Unix file mode in the string form “nnnn”. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;0666&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default group ID for the file share (unless the files have another group ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default owner ID for the file share (unless the files have another owner ID specified). Defaults to <code class="docutils literal notranslate"><span class="pre">65534</span></code> (<code class="docutils literal notranslate"><span class="pre">nfsnobody</span></code>). Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> through <code class="docutils literal notranslate"><span class="pre">4294967294</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.NfsFileShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.NfsFileShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.SmbFileShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">SmbFileShare</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authentication=None</em>, <em class="sig-param">default_storage_class=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">guess_mime_type_enabled=None</em>, <em class="sig-param">invalid_user_lists=None</em>, <em class="sig-param">kms_encrypted=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">location_arn=None</em>, <em class="sig-param">object_acl=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">requester_pays=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">valid_user_lists=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway SMB File Share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method that users use to access the file share. Defaults to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code>.</p></li>
<li><p><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</p></li>
<li><p><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>invalid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are not allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p></li>
<li><p><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p></li>
<li><p><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</p></li>
<li><p><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>valid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the SMB File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.authentication">
<code class="sig-name descname">authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication method that users use to access the file share. Defaults to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.default_storage_class">
<code class="sig-name descname">default_storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.default_storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.fileshare_id">
<code class="sig-name descname">fileshare_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.fileshare_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the SMB File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the file gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.guess_mime_type_enabled">
<code class="sig-name descname">guess_mime_type_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.guess_mime_type_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.invalid_user_lists">
<code class="sig-name descname">invalid_user_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.invalid_user_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users in the Active Directory that are not allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.kms_encrypted">
<code class="sig-name descname">kms_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.kms_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.location_arn">
<code class="sig-name descname">location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the backed storage used for storing file data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.object_acl">
<code class="sig-name descname">object_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.object_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.read_only">
<code class="sig-name descname">read_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.requester_pays">
<code class="sig-name descname">requester_pays</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.requester_pays" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.valid_user_lists">
<code class="sig-name descname">valid_user_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.valid_user_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users in the Active Directory that are allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.SmbFileShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">authentication=None</em>, <em class="sig-param">default_storage_class=None</em>, <em class="sig-param">fileshare_id=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">guess_mime_type_enabled=None</em>, <em class="sig-param">invalid_user_lists=None</em>, <em class="sig-param">kms_encrypted=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">location_arn=None</em>, <em class="sig-param">object_acl=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">requester_pays=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">valid_user_lists=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SmbFileShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the SMB File Share.</p></li>
<li><p><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method that users use to access the file share. Defaults to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code>.</p></li>
<li><p><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p></li>
<li><p><strong>fileshare_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the SMB File Share.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</p></li>
<li><p><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>invalid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are not allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p></li>
<li><p><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p></li>
<li><p><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</p></li>
<li><p><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>valid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.SmbFileShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.SmbFileShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.UploadBuffer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">UploadBuffer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway upload buffer.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Storage Gateway API provides no method to remove an upload buffer disk. Destroying this resource does not perform any Storage Gateway actions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.UploadBuffer.disk_id">
<code class="sig-name descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.UploadBuffer.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.UploadBuffer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UploadBuffer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.UploadBuffer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.UploadBuffer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.WorkingStorage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">WorkingStorage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway working storage.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Storage Gateway API provides no method to remove a working storage disk. Destroying this resource does not perform any Storage Gateway actions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.WorkingStorage.disk_id">
<code class="sig-name descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.WorkingStorage.gateway_arn">
<code class="sig-name descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.WorkingStorage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">gateway_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkingStorage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.WorkingStorage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.WorkingStorage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.storagegateway.get_local_disk">
<code class="sig-prename descclassname">pulumi_aws.storagegateway.</code><code class="sig-name descname">get_local_disk</code><span class="sig-paren">(</span><em class="sig-param">disk_node=None</em>, <em class="sig-param">disk_path=None</em>, <em class="sig-param">gateway_arn=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.get_local_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Storage Gateway local disk. The disk identifier is useful for adding the disk as a cache or upload buffer to a gateway.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_node</strong> (<em>str</em>) – The device node of the local disk to retrieve. For example, <code class="docutils literal notranslate"><span class="pre">/dev/sdb</span></code>.</p></li>
<li><p><strong>disk_path</strong> (<em>str</em>) – The device path of the local disk to retrieve. For example, <code class="docutils literal notranslate"><span class="pre">/dev/xvdb</span></code> or <code class="docutils literal notranslate"><span class="pre">/dev/nvme1n1</span></code>.</p></li>
<li><p><strong>gateway_arn</strong> (<em>str</em>) – The Amazon Resource Name (ARN) of the gateway.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/storagegateway_local_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/storagegateway_local_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
