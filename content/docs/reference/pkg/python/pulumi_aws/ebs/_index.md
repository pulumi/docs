---
---

<div class="section" id="ebs">
<h1>ebs<a class="headerlink" href="#ebs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ebs"></span><dl class="class">
<dt id="pulumi_aws.ebs.DefaultKmsKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">DefaultKmsKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>key_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the default customer master key (CMK) that your AWS account uses to encrypt EBS volumes.</p>
<p>Your AWS account has an AWS-managed default CMK that is used for encrypting an EBS volume when no CMK is specified in the API call that creates the volume.
By using the <code class="docutils literal notranslate"><span class="pre">aws_ebs_default_kms_key</span></code> resource, you can specify a customer-managed CMK to use in place of the AWS-managed default CMK.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Creating an <code class="docutils literal notranslate"><span class="pre">aws_ebs_default_kms_key</span></code> resource does not enable default EBS encryption. Use the <code class="docutils literal notranslate"><span class="pre">aws_ebs_encryption_by_default</span></code> to enable default EBS encryption.</p>
<p><strong>NOTE:</strong> Destroying this resource will reset the default CMK to the account’s AWS-managed default CMK for EBS.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_default_kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_default_kms_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ebs.DefaultKmsKey.key_arn">
<code class="descname">key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.DefaultKmsKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.DefaultKmsKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.EncryptionByDefault">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">EncryptionByDefault</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EncryptionByDefault resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not default EBS encryption is enabled. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_encryption_by_default.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_encryption_by_default.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ebs.EncryptionByDefault.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not default EBS encryption is enabled. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.EncryptionByDefault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.EncryptionByDefault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">GetDefaultKmsKeyResult</code><span class="sig-paren">(</span><em>key_arn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultKmsKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult.key_arn">
<code class="descname">key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult.key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the default KMS key uses to encrypt an EBS volume in this region when no key is specified in an API call that creates the volume and encryption by default is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">GetEncryptionByDefaultResult</code><span class="sig-paren">(</span><em>enabled=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEncryptionByDefault.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not default EBS encryption is enabled. Returns as <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetSnapshotIdsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">GetSnapshotIdsResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>owners=None</em>, <em>restorable_by_user_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshotIds.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotIdsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">GetSnapshotResult</code><span class="sig-paren">(</span><em>data_encryption_key_id=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>filters=None</em>, <em>kms_key_id=None</em>, <em>most_recent=None</em>, <em>owner_alias=None</em>, <em>owner_id=None</em>, <em>owners=None</em>, <em>restorable_by_user_ids=None</em>, <em>snapshot_id=None</em>, <em>snapshot_ids=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>volume_id=None</em>, <em>volume_size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.data_encryption_key_id">
<code class="descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the snapshot</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.owner_alias">
<code class="descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the EBS snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID (e.g. snap-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID (e.g. vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.volume_size">
<code class="descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetVolumeResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">GetVolumeResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>availability_zone=None</em>, <em>encrypted=None</em>, <em>filters=None</em>, <em>iops=None</em>, <em>kms_key_id=None</em>, <em>most_recent=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>tags=None</em>, <em>volume_id=None</em>, <em>volume_type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ where the EBS volume exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the disk is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of IOPS for the disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot_id the EBS volume is based off.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID (e.g. vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.volume_type">
<code class="descname">volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of EBS volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.Snapshot">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">Snapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>tags=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Snapshot of an EBS Volume.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the snapshot</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Volume ID of which to make a snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.data_encryption_key_id">
<code class="descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of what the snapshot is.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.owner_alias">
<code class="descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the EBS snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the snapshot</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Volume ID of which to make a snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.volume_size">
<code class="descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Snapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Snapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.SnapshotCopy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">SnapshotCopy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>kms_key_id=None</em>, <em>source_region=None</em>, <em>source_snapshot_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Snapshot of a snapshot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the snapshot is encrypted.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags for the snapshot.</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot_copy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot_copy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.data_encryption_key_id">
<code class="descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">source_snapshot_id</span></code> The ARN of the copied snapshot.</li>
<li><code class="docutils literal notranslate"><span class="pre">source_region</span></code> The region of the source snapshot.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of what the snapshot is.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">source_snapshot_id</span></code> The ARN for the snapshot to be copied.</li>
<li><code class="docutils literal notranslate"><span class="pre">source_region</span></code> The region of the source snapshot.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.owner_alias">
<code class="descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.volume_size">
<code class="descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.SnapshotCopy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.SnapshotCopy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Volume">
<em class="property">class </em><code class="descclassname">pulumi_aws.ebs.</code><code class="descname">Volume</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>encrypted=None</em>, <em>iops=None</em>, <em>kms_key_id=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single EBS volume.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ where the EBS volume will exist.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted.</li>
<li><strong>iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of IOPS to provision for the disk.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypted</span></code> needs to be set to true.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the drive in GiBs.</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot to base the EBS volume off of.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of EBS volume. Can be “standard”, “gp2”, “io1”, “sc1” or “st1” (Default: “standard”).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_volume.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ where the EBS volume will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the disk will be encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.iops">
<code class="descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of IOPS to provision for the disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A snapshot to base the EBS volume off of.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of EBS volume. Can be “standard”, “gp2”, “io1”, “sc1” or “st1” (Default: “standard”).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Volume.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Volume.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.get_default_kms_key">
<code class="descclassname">pulumi_aws.ebs.</code><code class="descname">get_default_kms_key</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_default_kms_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the default EBS encryption KMS key in the current region.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_default_kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_default_kms_key.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_encryption_by_default">
<code class="descclassname">pulumi_aws.ebs.</code><code class="descname">get_encryption_by_default</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_encryption_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a way to check whether default EBS encryption is enabled for your AWS account in the current AWS region.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_encryption_by_default.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_encryption_by_default.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_snapshot">
<code class="descclassname">pulumi_aws.ebs.</code><code class="descname">get_snapshot</code><span class="sig-paren">(</span><em>filters=None</em>, <em>most_recent=None</em>, <em>owners=None</em>, <em>restorable_by_user_ids=None</em>, <em>snapshot_ids=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an EBS Snapshot for use when provisioning EBS Volumes</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_snapshot_ids">
<code class="descclassname">pulumi_aws.ebs.</code><code class="descname">get_snapshot_ids</code><span class="sig-paren">(</span><em>filters=None</em>, <em>owners=None</em>, <em>restorable_by_user_ids=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_snapshot_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of EBS Snapshot IDs matching the specified
criteria.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot_ids.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot_ids.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_volume">
<code class="descclassname">pulumi_aws.ebs.</code><code class="descname">get_volume</code><span class="sig-paren">(</span><em>filters=None</em>, <em>most_recent=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an EBS volume for use in other
resources.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_volume.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
