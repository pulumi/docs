---
title: Module ebs
title_tag: Module ebs | Package pulumi_aws | Python SDK
linktitle: ebs
notitle: true
---

<div class="section" id="ebs">
<h1>ebs<a class="headerlink" href="#ebs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ebs"></span><dl class="class">
<dt id="pulumi_aws.ebs.AwaitableGetDefaultKmsKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">AwaitableGetDefaultKmsKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">key_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.AwaitableGetDefaultKmsKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.AwaitableGetEncryptionByDefaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">AwaitableGetEncryptionByDefaultResult</code><span class="sig-paren">(</span><em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.AwaitableGetEncryptionByDefaultResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.AwaitableGetSnapshotIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">AwaitableGetSnapshotIdsResult</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.AwaitableGetSnapshotIdsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">data_encryption_key_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">owner_alias=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_ids=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">iops=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.DefaultKmsKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">DefaultKmsKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the default customer master key (CMK) that your AWS account uses to encrypt EBS volumes.</p>
<p>Your AWS account has an AWS-managed default CMK that is used for encrypting an EBS volume when no CMK is specified in the API call that creates the volume.
By using the <code class="docutils literal notranslate"><span class="pre">ebs.DefaultKmsKey</span></code> resource, you can specify a customer-managed CMK to use in place of the AWS-managed default CMK.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Creating an <code class="docutils literal notranslate"><span class="pre">ebs.DefaultKmsKey</span></code> resource does not enable default EBS encryption. Use the <code class="docutils literal notranslate"><span class="pre">ebs.EncryptionByDefault</span></code> to enable default EBS encryption.</p>
<p><strong>NOTE:</strong> Destroying this resource will reset the default CMK to the account’s AWS-managed default CMK for EBS.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_default_kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_default_kms_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ebs.DefaultKmsKey.key_arn">
<code class="sig-name descname">key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.DefaultKmsKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultKmsKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.DefaultKmsKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.DefaultKmsKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.DefaultKmsKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.EncryptionByDefault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">EncryptionByDefault</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage whether default EBS encryption is enabled for your AWS account in the current AWS region. To manage the default KMS key for the region, see the <cite>``ebs.DefaultKmsKey`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ebs_default_kms_key.html">https://www.terraform.io/docs/providers/aws/r/ebs_default_kms_key.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Removing this resource disables default EBS encryption.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_encryption_by_default.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_encryption_by_default.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not default EBS encryption is enabled. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ebs.EncryptionByDefault.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not default EBS encryption is enabled. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.EncryptionByDefault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EncryptionByDefault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not default EBS encryption is enabled. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.EncryptionByDefault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.EncryptionByDefault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.EncryptionByDefault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">GetDefaultKmsKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">key_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultKmsKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetDefaultKmsKeyResult.key_arn">
<code class="sig-name descname">key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetDefaultKmsKeyResult.key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the default KMS key uses to encrypt an EBS volume in this region when no key is specified in an API call that creates the volume and encryption by default is enabled.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">GetEncryptionByDefaultResult</code><span class="sig-paren">(</span><em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEncryptionByDefault.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not default EBS encryption is enabled. Returns as <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetEncryptionByDefaultResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetEncryptionByDefaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetSnapshotIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">GetSnapshotIdsResult</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshotIds.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotIdsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">data_encryption_key_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">owner_alias=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_ids=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.data_encryption_key_id">
<code class="sig-name descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the snapshot</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.owner_alias">
<code class="sig-name descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the EBS snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID (e.g. snap-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.volume_id">
<code class="sig-name descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID (e.g. vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetSnapshotResult.volume_size">
<code class="sig-name descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetSnapshotResult.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">iops=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ where the EBS volume exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the disk is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.iops">
<code class="sig-name descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of IOPS for the disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot_id the EBS volume is based off.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.volume_id">
<code class="sig-name descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID (e.g. vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.GetVolumeResult.volume_type">
<code class="sig-name descname">volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.GetVolumeResult.volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of EBS volume.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ebs.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Snapshot of an EBS Volume.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the snapshot</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Volume ID of which to make a snapshot.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.data_encryption_key_id">
<code class="sig-name descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of what the snapshot is.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.owner_alias">
<code class="sig-name descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the EBS snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the snapshot</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.volume_id">
<code class="sig-name descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Volume ID of which to make a snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Snapshot.volume_size">
<code class="sig-name descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_encryption_key_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">owner_alias=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_encryption_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data encryption key identifier for the snapshot.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the snapshot is encrypted.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key.</p></li>
<li><p><strong>owner_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID of the EBS snapshot owner.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the snapshot</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Volume ID of which to make a snapshot.</p></li>
<li><p><strong>volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the drive in GiBs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.SnapshotCopy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">SnapshotCopy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">source_region=None</em>, <em class="sig-param">source_snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Snapshot of a snapshot.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot_copy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_snapshot_copy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the snapshot is encrypted.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `source_snapshot_id` The ARN for the snapshot to be copied.
* `source_region` The region of the source snapshot.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags for the snapshot.</p>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.data_encryption_key_id">
<code class="sig-name descname">data_encryption_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.data_encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data encryption key identifier for the snapshot.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">source_snapshot_id</span></code> The ARN of the copied snapshot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_region</span></code> The region of the source snapshot.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of what the snapshot is.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">source_snapshot_id</span></code> The ARN for the snapshot to be copied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_region</span></code> The region of the source snapshot.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.owner_alias">
<code class="sig-name descname">owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the snapshot owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags for the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.SnapshotCopy.volume_size">
<code class="sig-name descname">volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.SnapshotCopy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_encryption_key_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">owner_alias=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">source_region=None</em>, <em class="sig-param">source_snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">volume_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SnapshotCopy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_encryption_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data encryption key identifier for the snapshot.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `source_snapshot_id` The ARN of the copied snapshot.
* `source_region` The region of the source snapshot.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of what the snapshot is.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the snapshot is encrypted.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `source_snapshot_id` The ARN for the snapshot to be copied.
* `source_region` The region of the source snapshot.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>owner_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value from an Amazon-maintained list (<code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>) of snapshot owners.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID of the snapshot owner.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags for the snapshot.</p></li>
<li><p><strong>volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the drive in GiBs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.SnapshotCopy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.SnapshotCopy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.SnapshotCopy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">iops=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single EBS volume.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ebs_volume.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ where the EBS volume will exist.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted.</p></li>
<li><p><strong>iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of IOPS to provision for the disk.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the drive in GiBs.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot to base the EBS volume off of.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of EBS volume. Can be “standard”, “gp2”, “io1”, “sc1” or “st1” (Default: “gp2”).</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ where the EBS volume will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the disk will be encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.iops">
<code class="sig-name descname">iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of IOPS to provision for the disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypted</span></code> needs to be set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the drive in GiBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A snapshot to base the EBS volume off of.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ebs.Volume.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ebs.Volume.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of EBS volume. Can be “standard”, “gp2”, “io1”, “sc1” or “st1” (Default: “gp2”).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">iops=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ where the EBS volume will exist.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted.</p></li>
<li><p><strong>iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of IOPS to provision for the disk.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypted</span></code> needs to be set to true.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the drive in GiBs.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot to base the EBS volume off of.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of EBS volume. Can be “standard”, “gp2”, “io1”, “sc1” or “st1” (Default: “gp2”).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ebs.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ebs.get_default_kms_key">
<code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">get_default_kms_key</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_default_kms_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the default EBS encryption KMS key in the current region.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_default_kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_default_kms_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_encryption_by_default">
<code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">get_encryption_by_default</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_encryption_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a way to check whether default EBS encryption is enabled for your AWS account in the current AWS region.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_encryption_by_default.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_encryption_by_default.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_snapshot">
<code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em>, <em class="sig-param">snapshot_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an EBS Snapshot for use when provisioning EBS Volumes</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-snapshots in the AWS CLI reference][1].</p></li>
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most recent snapshot.</p></li>
<li><p><strong>owners</strong> (<em>list</em>) – Returns the snapshots owned by the specified owner id. Multiple owners can be specified.</p></li>
<li><p><strong>restorable_by_user_ids</strong> (<em>list</em>) – One or more AWS accounts IDs that can create volumes from the snapshot.</p></li>
<li><p><strong>snapshot_ids</strong> (<em>list</em>) – Returns information on a specific snapshot_id.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_snapshot_ids">
<code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">get_snapshot_ids</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">restorable_by_user_ids=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_snapshot_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of EBS Snapshot IDs matching the specified
criteria.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot_ids.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot_ids.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-volumes in the AWS CLI reference][1].</p></li>
<li><p><strong>owners</strong> (<em>list</em>) – Returns the snapshots owned by the specified owner id. Multiple owners can be specified.</p></li>
<li><p><strong>restorable_by_user_ids</strong> (<em>list</em>) – One or more AWS accounts IDs that can create volumes from the snapshot.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ebs.get_volume">
<code class="sig-prename descclassname">pulumi_aws.ebs.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ebs.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an EBS volume for use in other
resources.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_volume.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_volume.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-volumes in the AWS CLI reference][1].</p></li>
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most
recent Volume.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

</div>
