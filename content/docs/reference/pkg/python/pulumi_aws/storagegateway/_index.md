---
---

<div class="section" id="module-pulumi_aws.storagegateway">
<span id="storagegateway"></span><h1>storagegateway<a class="headerlink" href="#module-pulumi_aws.storagegateway" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.storagegateway.Cache">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">Cache</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disk_id=None</em>, <em>gateway_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Cache resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Cache.disk_id">
<code class="descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Cache.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Cache.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Cache.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Cache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">CachesIscsiVolume</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>gateway_arn=None</em>, <em>network_interface_id=None</em>, <em>snapshot_id=None</em>, <em>source_volume_arn=None</em>, <em>target_name=None</em>, <em>volume_size_in_bytes=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CachesIscsiVolume resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID of the snapshot to restore as the new cached volume. e.g. <code class="docutils literal notranslate"><span class="pre">snap-1122aabb</span></code>.</li>
<li><strong>source_volume_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume’s latest recovery point. The <code class="docutils literal notranslate"><span class="pre">volume_size_in_bytes</span></code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</li>
<li><strong>target_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.</li>
<li><strong>volume_size_in_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume in bytes.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.chap_enabled">
<code class="descname">chap_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.chap_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether mutual CHAP is enabled for the iSCSI target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.lun_number">
<code class="descname">lun_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.lun_number" title="Permalink to this definition">¶</a></dt>
<dd><p>Logical disk number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_port">
<code class="descname">network_interface_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.network_interface_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used to communicate with iSCSI targets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID of the snapshot to restore as the new cached volume. e.g. <code class="docutils literal notranslate"><span class="pre">snap-1122aabb</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.source_volume_arn">
<code class="descname">source_volume_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.source_volume_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume’s latest recovery point. The <code class="docutils literal notranslate"><span class="pre">volume_size_in_bytes</span></code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.target_arn">
<code class="descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Target Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.target_name">
<code class="descname">target_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.target_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_arn">
<code class="descname">volume_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume Amazon Resource Name (ARN), e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Volume ID, e.g. <code class="docutils literal notranslate"><span class="pre">vol-12345678</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.volume_size_in_bytes">
<code class="descname">volume_size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.volume_size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume in bytes.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.CachesIscsiVolume.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.CachesIscsiVolume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Gateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">Gateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>activation_key=None</em>, <em>gateway_ip_address=None</em>, <em>gateway_name=None</em>, <em>gateway_timezone=None</em>, <em>gateway_type=None</em>, <em>medium_changer_type=None</em>, <em>smb_active_directory_settings=None</em>, <em>smb_guest_password=None</em>, <em>tape_drive_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.</p>
<blockquote>
<div>NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving <code class="docutils literal notranslate"><span class="pre">The</span> <span class="pre">specified</span> <span class="pre">gateway</span> <span class="pre">is</span> <span class="pre">not</span> <span class="pre">connected</span></code> errors during resource creation (gateway activation), ensure your gateway instance meets the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html">Storage Gateway requirements</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>activation_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">gateway_ip_address</span></code>. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</li>
<li><strong>gateway_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the gateway.</li>
<li><strong>gateway_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time zone for the gateway. The time zone is of the format “GMT”, “GMT-hr:mm”, or “GMT+hr:mm”. For example, <code class="docutils literal notranslate"><span class="pre">GMT-4:00</span></code> indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway’s maintenance schedule.</li>
<li><strong>gateway_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the gateway. The default value is <code class="docutils literal notranslate"><span class="pre">STORED</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">CACHED</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code>, <code class="docutils literal notranslate"><span class="pre">STORED</span></code>, <code class="docutils literal notranslate"><span class="pre">VTL</span></code>.</li>
<li><strong>smb_active_directory_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code> authentication SMB file shares. More details below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.activation_key">
<code class="descname">activation_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.activation_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">gateway_ip_address</span></code>. Additional information is available in the <a class="reference external" href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Storage Gateway User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_id">
<code class="descname">gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_name">
<code class="descname">gateway_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_timezone">
<code class="descname">gateway_timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Time zone for the gateway. The time zone is of the format “GMT”, “GMT-hr:mm”, or “GMT+hr:mm”. For example, <code class="docutils literal notranslate"><span class="pre">GMT-4:00</span></code> indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway’s maintenance schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.gateway_type">
<code class="descname">gateway_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the gateway. The default value is <code class="docutils literal notranslate"><span class="pre">STORED</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">CACHED</span></code>, <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code>, <code class="docutils literal notranslate"><span class="pre">STORED</span></code>, <code class="docutils literal notranslate"><span class="pre">VTL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.Gateway.smb_active_directory_settings">
<code class="descname">smb_active_directory_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.smb_active_directory_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for <code class="docutils literal notranslate"><span class="pre">FILE_S3</span></code> gateway type. Must be set before creating <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code> authentication SMB file shares. More details below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.Gateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.Gateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.Gateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">GetLocalDiskResult</code><span class="sig-paren">(</span><em>disk_id=None</em>, <em>disk_node=None</em>, <em>disk_path=None</em>, <em>gateway_arn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocalDisk.</p>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult.disk_id">
<code class="descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk identifier. e.g. <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.GetLocalDiskResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.GetLocalDiskResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.storagegateway.NfsFileShare">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">NfsFileShare</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>client_lists=None</em>, <em>default_storage_class=None</em>, <em>gateway_arn=None</em>, <em>guess_mime_type_enabled=None</em>, <em>kms_encrypted=None</em>, <em>kms_key_arn=None</em>, <em>location_arn=None</em>, <em>nfs_file_share_defaults=None</em>, <em>object_acl=None</em>, <em>read_only=None</em>, <em>requester_pays=None</em>, <em>role_arn=None</em>, <em>squash=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway NFS File Share.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>client_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to <code class="docutils literal notranslate"><span class="pre">[&quot;0.0.0.0/0&quot;]</span></code> to not limit access. Minimum 1 item. Maximum 100 items.</li>
<li><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</li>
<li><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</li>
<li><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</li>
<li><strong>nfs_file_share_defaults</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with file share default values. More information below.</li>
<li><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</li>
<li><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</li>
<li><strong>squash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maps a user to anonymous user. Defaults to <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code> (only root is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">NoSquash</span></code> (no one is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">AllSquash</span></code> (everyone is mapped to anonymous user)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the NFS File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.client_lists">
<code class="descname">client_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.client_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to <code class="docutils literal notranslate"><span class="pre">[&quot;0.0.0.0/0&quot;]</span></code> to not limit access. Minimum 1 item. Maximum 100 items.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.default_storage_class">
<code class="descname">default_storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.default_storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.fileshare_id">
<code class="descname">fileshare_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.fileshare_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the NFS File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the file gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.guess_mime_type_enabled">
<code class="descname">guess_mime_type_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.guess_mime_type_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.kms_encrypted">
<code class="descname">kms_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.kms_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.location_arn">
<code class="descname">location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the backed storage used for storing file data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.nfs_file_share_defaults">
<code class="descname">nfs_file_share_defaults</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.nfs_file_share_defaults" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument with file share default values. More information below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.object_acl">
<code class="descname">object_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.object_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.read_only">
<code class="descname">read_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.requester_pays">
<code class="descname">requester_pays</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.requester_pays" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.NfsFileShare.squash">
<code class="descname">squash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.squash" title="Permalink to this definition">¶</a></dt>
<dd><p>Maps a user to anonymous user. Defaults to <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">RootSquash</span></code> (only root is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">NoSquash</span></code> (no one is mapped to anonymous user), <code class="docutils literal notranslate"><span class="pre">AllSquash</span></code> (everyone is mapped to anonymous user)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.NfsFileShare.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.NfsFileShare.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.NfsFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.SmbFileShare">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">SmbFileShare</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>authentication=None</em>, <em>default_storage_class=None</em>, <em>gateway_arn=None</em>, <em>guess_mime_type_enabled=None</em>, <em>invalid_user_lists=None</em>, <em>kms_encrypted=None</em>, <em>kms_key_arn=None</em>, <em>location_arn=None</em>, <em>object_acl=None</em>, <em>read_only=None</em>, <em>requester_pays=None</em>, <em>role_arn=None</em>, <em>valid_user_lists=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Storage Gateway SMB File Share.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method that users use to access the file share. Defaults to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code>.</li>
<li><strong>default_storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the file gateway.</li>
<li><strong>guess_mime_type_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>invalid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are not allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</li>
<li><strong>kms_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</li>
<li><strong>location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the backed storage used for storing file data.</li>
<li><strong>object_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</li>
<li><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>requester_pays</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</li>
<li><strong>valid_user_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users in the Active Directory that are allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_smb_file_share.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the SMB File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.authentication">
<code class="descname">authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication method that users use to access the file share. Defaults to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">GuestAccess</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.default_storage_class">
<code class="descname">default_storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.default_storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">S3_STANDARD</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_STANDARD_IA</span></code>, <code class="docutils literal notranslate"><span class="pre">S3_ONEZONE_IA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.fileshare_id">
<code class="descname">fileshare_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.fileshare_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the SMB File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the file gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.guess_mime_type_enabled">
<code class="descname">guess_mime_type_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.guess_mime_type_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.invalid_user_lists">
<code class="descname">invalid_user_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.invalid_user_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users in the Active Directory that are not allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.kms_encrypted">
<code class="descname">kms_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.kms_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value if <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon S3 server side encryption with your own AWS KMS key, or <code class="docutils literal notranslate"><span class="pre">false</span></code> to use a key managed by Amazon S3. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when <code class="docutils literal notranslate"><span class="pre">kms_encrypted</span></code> is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.location_arn">
<code class="descname">location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the backed storage used for storing file data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.object_acl">
<code class="descname">object_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.object_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Control List permission for S3 bucket objects. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.read_only">
<code class="descname">read_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to indicate write status of file share. File share does not accept writes if <code class="docutils literal notranslate"><span class="pre">true</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.requester_pays">
<code class="descname">requester_pays</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.requester_pays" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want the requester to pay instead of the bucket owner. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.SmbFileShare.valid_user_lists">
<code class="descname">valid_user_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.valid_user_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users in the Active Directory that are allowed to access the file share. Only valid if <code class="docutils literal notranslate"><span class="pre">authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ActiveDirectory</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.SmbFileShare.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.SmbFileShare.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.SmbFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.UploadBuffer">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">UploadBuffer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disk_id=None</em>, <em>gateway_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UploadBuffer resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_upload_buffer.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.UploadBuffer.disk_id">
<code class="descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.UploadBuffer.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.UploadBuffer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.UploadBuffer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.UploadBuffer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.WorkingStorage">
<em class="property">class </em><code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">WorkingStorage</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disk_id=None</em>, <em>gateway_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a WorkingStorage resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</li>
<li><strong>gateway_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_working_storage.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.storagegateway.WorkingStorage.disk_id">
<code class="descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Local disk identifier. For example, <code class="docutils literal notranslate"><span class="pre">pci-0000:03:00.0-scsi-0:0:0:0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.storagegateway.WorkingStorage.gateway_arn">
<code class="descname">gateway_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.gateway_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.storagegateway.WorkingStorage.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.WorkingStorage.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.WorkingStorage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.storagegateway.get_local_disk">
<code class="descclassname">pulumi_aws.storagegateway.</code><code class="descname">get_local_disk</code><span class="sig-paren">(</span><em>disk_node=None</em>, <em>disk_path=None</em>, <em>gateway_arn=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.storagegateway.get_local_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Storage Gateway local disk. The disk identifier is useful for adding the disk as a cache or upload buffer to a gateway.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/storagegateway_local_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/storagegateway_local_disk.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
