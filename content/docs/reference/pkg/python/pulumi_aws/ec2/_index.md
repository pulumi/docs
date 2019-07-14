---
---

<div class="section" id="ec2">
<h1>ec2<a class="headerlink" href="#ec2" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ec2"></span><dl class="class">
<dt id="pulumi_aws.ec2.Ami">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Ami</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>architecture=None</em>, <em>description=None</em>, <em>ebs_block_devices=None</em>, <em>ena_support=None</em>, <em>ephemeral_block_devices=None</em>, <em>image_location=None</em>, <em>kernel_id=None</em>, <em>name=None</em>, <em>ramdisk_id=None</em>, <em>root_device_name=None</em>, <em>sriov_net_support=None</em>, <em>tags=None</em>, <em>virtualization_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Ami" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI resource allows the creation and management of a completely-custom
<em>Amazon Machine Image</em> (AMI).</p>
<p>If you just want to duplicate an existing AMI, possibly copying it to another
region, it’s better to use <code class="docutils literal notranslate"><span class="pre">aws_ami_copy</span></code> instead.</p>
<p>If you just want to share an existing AMI with another AWS account,
it’s better to use <code class="docutils literal notranslate"><span class="pre">aws_ami_launch_permission</span></code> instead.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances. Defaults to “x86_64”.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A longer, human-readable description for the AMI.</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</li>
<li><strong>ena_support</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether enhanced networking with ENA is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</li>
<li><strong>image_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to an S3 object containing an image manifest, e.g. created
by the <code class="docutils literal notranslate"><span class="pre">ec2-upload-bundle</span></code> command in the EC2 command line tools.</li>
<li><strong>kernel_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</li>
<li><strong>ramdisk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of an initrd image (ARI) that will be used when booting the
created instances.</li>
<li><strong>root_device_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the root device (for example, <code class="docutils literal notranslate"><span class="pre">/dev/sda1</span></code>, or <code class="docutils literal notranslate"><span class="pre">/dev/xvda</span></code>).</li>
<li><strong>sriov_net_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When set to “simple” (the default), enables enhanced networking
for created instances. No other value is supported at this time.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>virtualization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword to choose what virtualization mode created instances
will use. Can be either “paravirtual” (the default) or “hvm”. The choice of virtualization type
changes the set of further arguments that are required, as described below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.architecture">
<code class="descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances. Defaults to “x86_64”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A longer, human-readable description for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.ena_support">
<code class="descname">ena_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.ena_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether enhanced networking with ENA is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.image_location">
<code class="descname">image_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.image_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to an S3 object containing an image manifest, e.g. created
by the <code class="docutils literal notranslate"><span class="pre">ec2-upload-bundle</span></code> command in the EC2 command line tools.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.kernel_id">
<code class="descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.ramdisk_id">
<code class="descname">ramdisk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.ramdisk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of an initrd image (ARI) that will be used when booting the
created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.root_device_name">
<code class="descname">root_device_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.root_device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the root device (for example, <code class="docutils literal notranslate"><span class="pre">/dev/sda1</span></code>, or <code class="docutils literal notranslate"><span class="pre">/dev/xvda</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.root_snapshot_id">
<code class="descname">root_snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.root_snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Snapshot ID for the root volume (for EBS-backed AMIs)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.sriov_net_support">
<code class="descname">sriov_net_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.sriov_net_support" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to “simple” (the default), enables enhanced networking
for created instances. No other value is supported at this time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Ami.virtualization_type">
<code class="descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Ami.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either “paravirtual” (the default) or “hvm”. The choice of virtualization type
changes the set of further arguments that are required, as described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Ami.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Ami.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Ami.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Ami.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiCopy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">AmiCopy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>ebs_block_devices=None</em>, <em>encrypted=None</em>, <em>ephemeral_block_devices=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>source_ami_id=None</em>, <em>source_ami_region=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy" title="Permalink to this definition">¶</a></dt>
<dd><p>The “AMI copy” resource allows duplication of an Amazon Machine Image (AMI),
including cross-region copies.</p>
<p>If the source AMI has associated EBS snapshots, those will also be duplicated
along with the AMI.</p>
<p>This is useful for taking a single AMI provisioned in one region and making
it available in another for a multi-region deployment.</p>
<p>Copying an AMI can take several minutes. The creation of this resource will
block until the new AMI is available for use on new instances.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A longer, human-readable description for the AMI.</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</li>
<li><strong>source_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the AMI to copy. This id must be valid in the region
given by <code class="docutils literal notranslate"><span class="pre">source_ami_region</span></code>.</li>
<li><strong>source_ami_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_copy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_copy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.architecture">
<code class="descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances. Defaults to “x86_64”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A longer, human-readable description for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.ena_support">
<code class="descname">ena_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.ena_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether enhanced networking with ENA is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.image_location">
<code class="descname">image_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.image_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to an S3 object containing an image manifest, e.g. created
by the <code class="docutils literal notranslate"><span class="pre">ec2-upload-bundle</span></code> command in the EC2 command line tools.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.kernel_id">
<code class="descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.ramdisk_id">
<code class="descname">ramdisk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.ramdisk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of an initrd image (ARI) that will be used when booting the
created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.root_device_name">
<code class="descname">root_device_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.root_device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the root device (for example, <code class="docutils literal notranslate"><span class="pre">/dev/sda1</span></code>, or <code class="docutils literal notranslate"><span class="pre">/dev/xvda</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.source_ami_id">
<code class="descname">source_ami_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.source_ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the AMI to copy. This id must be valid in the region
given by <code class="docutils literal notranslate"><span class="pre">source_ami_region</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.source_ami_region">
<code class="descname">source_ami_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.source_ami_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.sriov_net_support">
<code class="descname">sriov_net_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.sriov_net_support" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to “simple” (the default), enables enhanced networking
for created instances. No other value is supported at this time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiCopy.virtualization_type">
<code class="descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either “paravirtual” (the default) or “hvm”. The choice of virtualization type
changes the set of further arguments that are required, as described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.AmiCopy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiCopy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiCopy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiFromInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">AmiFromInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>ebs_block_devices=None</em>, <em>ephemeral_block_devices=None</em>, <em>name=None</em>, <em>snapshot_without_reboot=None</em>, <em>source_instance_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>The “AMI from instance” resource allows the creation of an Amazon Machine
Image (AMI) modelled after an existing EBS-backed EC2 instance.</p>
<p>The created AMI will refer to implicitly-created snapshots of the instance’s
EBS volumes and mimick its assigned block device configuration at the time
the resource is created.</p>
<p>This resource is best applied to an instance that is stopped when this instance
is created, so that the contents of the created image are predictable. When
applied to an instance that is running, <em>the instance will be stopped before taking
the snapshots and then started back up again</em>, resulting in a period of
downtime.</p>
<p>Note that the source instance is inspected only at the initial creation of this
resource. Ongoing updates to the referenced instance will not be propagated into
the generated AMI. Users may taint or otherwise recreate the resource in order
to produce a fresh snapshot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A longer, human-readable description for the AMI.</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</li>
<li><strong>snapshot_without_reboot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that overrides the behavior of stopping
the instance before snapshotting. This is risky since it may cause a snapshot of an
inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
guarantees that no filesystem writes will be underway at the time of snapshot.</li>
<li><strong>source_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the instance to use as the basis of the AMI.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_from_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_from_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.architecture">
<code class="descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances. Defaults to “x86_64”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A longer, human-readable description for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.ena_support">
<code class="descname">ena_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.ena_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether enhanced networking with ENA is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.image_location">
<code class="descname">image_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.image_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to an S3 object containing an image manifest, e.g. created
by the <code class="docutils literal notranslate"><span class="pre">ec2-upload-bundle</span></code> command in the EC2 command line tools.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.kernel_id">
<code class="descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.ramdisk_id">
<code class="descname">ramdisk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.ramdisk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of an initrd image (ARI) that will be used when booting the
created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.root_device_name">
<code class="descname">root_device_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.root_device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the root device (for example, <code class="docutils literal notranslate"><span class="pre">/dev/sda1</span></code>, or <code class="docutils literal notranslate"><span class="pre">/dev/xvda</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.snapshot_without_reboot">
<code class="descname">snapshot_without_reboot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.snapshot_without_reboot" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean that overrides the behavior of stopping
the instance before snapshotting. This is risky since it may cause a snapshot of an
inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
guarantees that no filesystem writes will be underway at the time of snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.source_instance_id">
<code class="descname">source_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.source_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the instance to use as the basis of the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.sriov_net_support">
<code class="descname">sriov_net_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.sriov_net_support" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to “simple” (the default), enables enhanced networking
for created instances. No other value is supported at this time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiFromInstance.virtualization_type">
<code class="descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either “paravirtual” (the default) or “hvm”. The choice of virtualization type
changes the set of further arguments that are required, as described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.AmiFromInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiFromInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiFromInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiLaunchPermission">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">AmiLaunchPermission</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>image_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiLaunchPermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds launch permission to Amazon Machine Image (AMI) from another AWS account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An AWS Account ID to add launch permissions.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_launch_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_launch_permission.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiLaunchPermission.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiLaunchPermission.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An AWS Account ID to add launch permissions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.AmiLaunchPermission.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.AmiLaunchPermission.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.AmiLaunchPermission.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiLaunchPermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.AmiLaunchPermission.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.AmiLaunchPermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.CapacityReservation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">CapacityReservation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>ebs_optimized=None</em>, <em>end_date=None</em>, <em>end_date_type=None</em>, <em>ephemeral_storage=None</em>, <em>instance_count=None</em>, <em>instance_match_criteria=None</em>, <em>instance_platform=None</em>, <em>instance_type=None</em>, <em>tags=None</em>, <em>tenancy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EC2 Capacity Reservation. This allows you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone in which to create the Capacity Reservation.</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the Capacity Reservation supports EBS-optimized instances.</li>
<li><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</li>
<li><strong>end_date_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates the way in which the Capacity Reservation ends. Specify either <code class="docutils literal notranslate"><span class="pre">unlimited</span></code> or <code class="docutils literal notranslate"><span class="pre">limited</span></code>.</li>
<li><strong>ephemeral_storage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.</li>
<li><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances for which to reserve capacity.</li>
<li><strong>instance_match_criteria</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates the type of instance launches that the Capacity Reservation accepts. Specify either <code class="docutils literal notranslate"><span class="pre">open</span></code> or <code class="docutils literal notranslate"><span class="pre">targeted</span></code>.</li>
<li><strong>instance_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of operating system for which to reserve capacity. Valid options are <code class="docutils literal notranslate"><span class="pre">Linux/UNIX</span></code>, <code class="docutils literal notranslate"><span class="pre">Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Enterprise</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Web</span></code>.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance type for which to reserve capacity.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates the tenancy of the Capacity Reservation. Specify either <code class="docutils literal notranslate"><span class="pre">default</span></code> or <code class="docutils literal notranslate"><span class="pre">dedicated</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_capacity_reservation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_capacity_reservation.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone in which to create the Capacity Reservation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the Capacity Reservation supports EBS-optimized instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.end_date">
<code class="descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.end_date_type">
<code class="descname">end_date_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.end_date_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the way in which the Capacity Reservation ends. Specify either <code class="docutils literal notranslate"><span class="pre">unlimited</span></code> or <code class="docutils literal notranslate"><span class="pre">limited</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.ephemeral_storage">
<code class="descname">ephemeral_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.ephemeral_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.instance_count">
<code class="descname">instance_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances for which to reserve capacity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.instance_match_criteria">
<code class="descname">instance_match_criteria</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.instance_match_criteria" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the type of instance launches that the Capacity Reservation accepts. Specify either <code class="docutils literal notranslate"><span class="pre">open</span></code> or <code class="docutils literal notranslate"><span class="pre">targeted</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.instance_platform">
<code class="descname">instance_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.instance_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of operating system for which to reserve capacity. Valid options are <code class="docutils literal notranslate"><span class="pre">Linux/UNIX</span></code>, <code class="docutils literal notranslate"><span class="pre">Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Enterprise</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">with</span> <span class="pre">SQL</span> <span class="pre">Server</span> <span class="pre">Web</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type for which to reserve capacity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CapacityReservation.tenancy">
<code class="descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the tenancy of the Capacity Reservation. Specify either <code class="docutils literal notranslate"><span class="pre">default</span></code> or <code class="docutils literal notranslate"><span class="pre">dedicated</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.CapacityReservation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.CapacityReservation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CapacityReservation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.CustomerGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">CustomerGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bgp_asn=None</em>, <em>ip_address=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a customer gateway inside a VPC. These objects can be connected to VPN gateways via VPN connections, and allow you to establish tunnels between your network and the VPC.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The gateway’s Border Gateway Protocol (BGP) Autonomous System Number (ASN).</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the gateway’s Internet-routable external interface.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Tags to apply to the gateway.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of customer gateway. The only type AWS
supports at this time is “ipsec.1”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/customer_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/customer_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.CustomerGateway.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The gateway’s Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CustomerGateway.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway’s Internet-routable external interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CustomerGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to apply to the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.CustomerGateway.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of customer gateway. The only type AWS
supports at this time is “ipsec.1”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.CustomerGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.CustomerGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.CustomerGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultNetworkAcl">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultNetworkAcl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_network_acl_id=None</em>, <em>egress=None</em>, <em>ingress=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultNetworkAcl resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_network_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network ACL ID to manage. This
attribute is exported from <code class="docutils literal notranslate"><span class="pre">aws_vpc</span></code>, or manually found via the AWS Console.</li>
<li><strong>egress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an egress rule. Parameters defined below.</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an ingress rule. Parameters defined below.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_network_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_network_acl.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.default_network_acl_id">
<code class="descname">default_network_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.default_network_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network ACL ID to manage. This
attribute is exported from <code class="docutils literal notranslate"><span class="pre">aws_vpc</span></code>, or manually found via the AWS Console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.egress">
<code class="descname">egress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.egress" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an egress rule. Parameters defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an ingress rule. Parameters defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the Default Network ACL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated VPC</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultNetworkAcl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultNetworkAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultRouteTable">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultRouteTable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_route_table_id=None</em>, <em>propagating_vgws=None</em>, <em>routes=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultRouteTable resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Default Routing Table.</li>
<li><strong>propagating_vgws</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual gateways for propagation.</li>
<li><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of route objects. Their keys are documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_route_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_route_table.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultRouteTable.default_route_table_id">
<code class="descname">default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Default Routing Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultRouteTable.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultRouteTable.propagating_vgws">
<code class="descname">propagating_vgws</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.propagating_vgws" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of virtual gateways for propagation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultRouteTable.routes">
<code class="descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of route objects. Their keys are documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultRouteTable.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultRouteTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultRouteTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultRouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultSecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultSecurityGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>egress=None</em>, <em>ingress=None</em>, <em>revoke_rules_on_delete=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultSecurityGroup resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>egress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID. <strong>Note that changing
the ``vpc_id`` will *not* restore any default security group rules that were
modified, added, or removed.</strong> It will be left in its current state</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_security_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.egress">
<code class="descname">egress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.egress" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID. <strong>Note that changing
the ``vpc_id`` will *not* restore any default security group rules that were
modified, added, or removed.</strong> It will be left in its current state</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultSecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultSubnet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultSubnet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>map_public_ip_on_launch=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultSubnet resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>map_public_ip_on_launch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_subnet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_subnet.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.map_public_ip_on_launch">
<code class="descname">map_public_ip_on_launch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.map_public_ip_on_launch" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultSubnet.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultSubnet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultSubnet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultSubnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultVpc">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultVpc</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enable_classiclink=None</em>, <em>enable_classiclink_dns_support=None</em>, <em>enable_dns_hostnames=None</em>, <em>enable_dns_support=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultVpc resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enable_classiclink</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.</li>
<li><strong>enable_dns_hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.</li>
<li><strong>enable_dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable DNS support in the VPC. Defaults true.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_vpc.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_vpc.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.assign_generated_ipv6_cidr_block">
<code class="descname">assign_generated_ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.assign_generated_ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC was assigned</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block of the VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.default_network_acl_id">
<code class="descname">default_network_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.default_network_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network ACL created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.default_route_table_id">
<code class="descname">default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the route table created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.default_security_group_id">
<code class="descname">default_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.default_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.enable_classiclink">
<code class="descname">enable_classiclink</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.enable_classiclink" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.enable_dns_hostnames">
<code class="descname">enable_dns_hostnames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.enable_dns_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.enable_dns_support">
<code class="descname">enable_dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.enable_dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable DNS support in the VPC. Defaults true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.instance_tenancy">
<code class="descname">instance_tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.instance_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenancy of instances spin up within VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.ipv6_association_id">
<code class="descname">ipv6_association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.ipv6_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The association ID for the IPv6 CIDR block of the VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 CIDR block of the VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.main_route_table_id">
<code class="descname">main_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.main_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the main route table associated with
this VPC. Note that you can change a VPC’s main route table by using an
<cite>``aws_main_route_table_association`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html">https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html</a>&gt;`_</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpc.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultVpc.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultVpc.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">DefaultVpcDhcpOptions</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>netbios_name_servers=None</em>, <em>netbios_node_type=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DefaultVpcDhcpOptions resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>netbios_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of NETBIOS name servers.</li>
<li><strong>netbios_node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see <a class="reference external" href="http://www.ietf.org/rfc/rfc2132.txt">RFC 2132</a>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_vpc_dhcp_options.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_vpc_dhcp_options.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.netbios_name_servers">
<code class="descname">netbios_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.netbios_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of NETBIOS name servers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.netbios_node_type">
<code class="descname">netbios_node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.netbios_node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see <a class="reference external" href="http://www.ietf.org/rfc/rfc2132.txt">RFC 2132</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the DHCP options set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.DefaultVpcDhcpOptions.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.DefaultVpcDhcpOptions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.EgressOnlyInternetGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">EgressOnlyInternetGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EgressOnlyInternetGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>[IPv6 only] Creates an egress-only Internet gateway for your VPC.
An egress-only Internet gateway is used to enable outbound communication
over IPv6 from instances in your VPC to the Internet, and prevents hosts
outside of your VPC from initiating an IPv6 connection with your instance.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID to create in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/egress_only_internet_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/egress_only_internet_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.EgressOnlyInternetGateway.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EgressOnlyInternetGateway.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID to create in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.EgressOnlyInternetGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EgressOnlyInternetGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.EgressOnlyInternetGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EgressOnlyInternetGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Eip">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Eip</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>associate_with_private_ip=None</em>, <em>instance=None</em>, <em>network_interface=None</em>, <em>public_ipv4_pool=None</em>, <em>tags=None</em>, <em>vpc=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Eip" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic IP resource.</p>
<blockquote>
<div><p><strong>Note:</strong> EIP may require IGW to exist prior to association. Use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> to set an explicit dependency on the IGW.</p>
<p><strong>Note:</strong> Do not use <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> to associate the EIP to <code class="docutils literal notranslate"><span class="pre">aws_lb</span></code> or <code class="docutils literal notranslate"><span class="pre">aws_nat_gateway</span></code> resources. Instead use the <code class="docutils literal notranslate"><span class="pre">allocation_id</span></code> available in those resources to allow AWS to manage the association, otherwise you will see <code class="docutils literal notranslate"><span class="pre">AuthFailure</span></code> errors.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>associate_with_private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EC2 instance ID.</li>
<li><strong>network_interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network interface ID to associate with.</li>
<li><strong>public_ipv4_pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EC2 IPv4 address pool identifier or <code class="docutils literal notranslate"><span class="pre">amazon</span></code>. This option is only available for VPC EIPs.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean if the EIP is in a VPC or not.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eip.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eip.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.associate_with_private_ip">
<code class="descname">associate_with_private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.associate_with_private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 instance ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.network_interface">
<code class="descname">network_interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.network_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>Network interface ID to associate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.private_dns">
<code class="descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The Private DNS associated with the Elastic IP address (if in VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the private IP address (if in VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.public_dns">
<code class="descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>Public DNS associated with the Elastic IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the public IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.public_ipv4_pool">
<code class="descname">public_ipv4_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.public_ipv4_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 IPv4 address pool identifier or <code class="docutils literal notranslate"><span class="pre">amazon</span></code>. This option is only available for VPC EIPs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Eip.vpc">
<code class="descname">vpc</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Eip.vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean if the EIP is in a VPC or not.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Eip.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Eip.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Eip.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Eip.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.EipAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">EipAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocation_id=None</em>, <em>allow_reassociation=None</em>, <em>instance_id=None</em>, <em>network_interface_id=None</em>, <em>private_ip_address=None</em>, <em>public_ip=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS EIP Association as a top level resource, to associate and
disassociate Elastic IPs from AWS Instances and Network Interfaces.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Do not use this resource to associate an EIP to <code class="docutils literal notranslate"><span class="pre">aws_lb</span></code> or <code class="docutils literal notranslate"><span class="pre">aws_nat_gateway</span></code> resources. Instead use the <code class="docutils literal notranslate"><span class="pre">allocation_id</span></code> available in those resources to allow AWS to manage the association, otherwise you will see <code class="docutils literal notranslate"><span class="pre">AuthFailure</span></code> errors.</p>
<p><strong>NOTE:</strong> <code class="docutils literal notranslate"><span class="pre">aws_eip_association</span></code> is useful in scenarios where EIPs are either
pre-existing or distributed to customers or users and therefore cannot be changed.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The allocation ID. This is required for EC2-VPC.</li>
<li><strong>allow_reassociation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow an Elastic IP to
be re-associated. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> in VPC.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.</li>
<li><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.</li>
<li><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Elastic IP address. This is required for EC2-Classic.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eip_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eip_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.allocation_id">
<code class="descname">allocation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.allocation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocation ID. This is required for EC2-VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.allow_reassociation">
<code class="descname">allow_reassociation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.allow_reassociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow an Elastic IP to
be re-associated. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> in VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.private_ip_address">
<code class="descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.EipAssociation.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Elastic IP address. This is required for EC2-Classic.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.EipAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.EipAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.EipAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Fleet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Fleet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>excess_capacity_termination_policy=None</em>, <em>launch_template_config=None</em>, <em>on_demand_options=None</em>, <em>replace_unhealthy_instances=None</em>, <em>spot_options=None</em>, <em>tags=None</em>, <em>target_capacity_specification=None</em>, <em>terminate_instances=None</em>, <em>terminate_instances_with_expiration=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Fleet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage EC2 Fleets.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>excess_capacity_termination_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code>, <code class="docutils literal notranslate"><span class="pre">termination</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">termination</span></code>.</li>
<li><strong>launch_template_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing EC2 Launch Template configurations. Defined below.</li>
<li><strong>on_demand_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing On-Demand configurations. Defined below.</li>
<li><strong>replace_unhealthy_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether EC2 Fleet should replace unhealthy instances. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>spot_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing Spot configurations. Defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.</li>
<li><strong>target_capacity_specification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing target capacity configurations. Defined below.</li>
<li><strong>terminate_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>terminate_instances_with_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether running instances should be terminated when the EC2 Fleet expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, <code class="docutils literal notranslate"><span class="pre">request</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">maintain</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_fleet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_fleet.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.excess_capacity_termination_policy">
<code class="descname">excess_capacity_termination_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.excess_capacity_termination_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code>, <code class="docutils literal notranslate"><span class="pre">termination</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">termination</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.launch_template_config">
<code class="descname">launch_template_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.launch_template_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing EC2 Launch Template configurations. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.on_demand_options">
<code class="descname">on_demand_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.on_demand_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing On-Demand configurations. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.replace_unhealthy_instances">
<code class="descname">replace_unhealthy_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.replace_unhealthy_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether EC2 Fleet should replace unhealthy instances. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.spot_options">
<code class="descname">spot_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.spot_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing Spot configurations. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.target_capacity_specification">
<code class="descname">target_capacity_specification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.target_capacity_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing target capacity configurations. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.terminate_instances">
<code class="descname">terminate_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.terminate_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.terminate_instances_with_expiration">
<code class="descname">terminate_instances_with_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.terminate_instances_with_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether running instances should be terminated when the EC2 Fleet expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Fleet.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Fleet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, <code class="docutils literal notranslate"><span class="pre">request</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">maintain</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Fleet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Fleet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Fleet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Fleet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.FlowLog">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">FlowLog</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eni_id=None</em>, <em>iam_role_arn=None</em>, <em>log_destination=None</em>, <em>log_destination_type=None</em>, <em>log_group_name=None</em>, <em>subnet_id=None</em>, <em>traffic_type=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.FlowLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group or a S3 Bucket.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eni_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic Network Interface ID to attach to</li>
<li><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the IAM role that’s used to post flow logs to a CloudWatch Logs log group</li>
<li><strong>log_destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the logging destination.</li>
<li><strong>log_destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the logging destination. Valid values: <code class="docutils literal notranslate"><span class="pre">cloud-watch-logs</span></code>, <code class="docutils literal notranslate"><span class="pre">s3</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">cloud-watch-logs</span></code>.</li>
<li><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">log_destination</span></code> instead. The name of the CloudWatch log group.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to attach to</li>
<li><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of traffic to capture. Valid values: <code class="docutils literal notranslate"><span class="pre">ACCEPT</span></code>,<code class="docutils literal notranslate"><span class="pre">REJECT</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC ID to attach to</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/flow_log.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/flow_log.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.eni_id">
<code class="descname">eni_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.eni_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic Network Interface ID to attach to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.iam_role_arn">
<code class="descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the IAM role that’s used to post flow logs to a CloudWatch Logs log group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.log_destination">
<code class="descname">log_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.log_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the logging destination.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.log_destination_type">
<code class="descname">log_destination_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.log_destination_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the logging destination. Valid values: <code class="docutils literal notranslate"><span class="pre">cloud-watch-logs</span></code>, <code class="docutils literal notranslate"><span class="pre">s3</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">cloud-watch-logs</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.log_group_name">
<code class="descname">log_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.log_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">log_destination</span></code> instead. The name of the CloudWatch log group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet ID to attach to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.traffic_type">
<code class="descname">traffic_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.traffic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of traffic to capture. Valid values: <code class="docutils literal notranslate"><span class="pre">ACCEPT</span></code>,<code class="docutils literal notranslate"><span class="pre">REJECT</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.FlowLog.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID to attach to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.FlowLog.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.FlowLog.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.FlowLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.GetCustomerGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetCustomerGatewayResult</code><span class="sig-paren">(</span><em>bgp_asn=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>ip_address=None</em>, <em>tags=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetCustomerGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomerGateway.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetCustomerGatewayResult.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetCustomerGatewayResult.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The gateway’s Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetCustomerGatewayResult.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetCustomerGatewayResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The IP address of the gateway’s Internet-routable external interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetCustomerGatewayResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetCustomerGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of key-value pairs assigned to the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetCustomerGatewayResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetCustomerGatewayResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The type of customer gateway. The only type AWS supports at this time is “ipsec.1”.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetInstanceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetInstanceResult</code><span class="sig-paren">(</span><em>ami=None</em>, <em>arn=None</em>, <em>associate_public_ip_address=None</em>, <em>availability_zone=None</em>, <em>credit_specifications=None</em>, <em>disable_api_termination=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>ephemeral_block_devices=None</em>, <em>filters=None</em>, <em>get_password_data=None</em>, <em>get_user_data=None</em>, <em>host_id=None</em>, <em>iam_instance_profile=None</em>, <em>instance_id=None</em>, <em>instance_state=None</em>, <em>instance_tags=None</em>, <em>instance_type=None</em>, <em>key_name=None</em>, <em>monitoring=None</em>, <em>network_interface_id=None</em>, <em>password_data=None</em>, <em>placement_group=None</em>, <em>private_dns=None</em>, <em>private_ip=None</em>, <em>public_dns=None</em>, <em>public_ip=None</em>, <em>root_block_devices=None</em>, <em>security_groups=None</em>, <em>source_dest_check=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>tenancy=None</em>, <em>user_data=None</em>, <em>user_data_base64=None</em>, <em>vpc_security_group_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.ami">
<code class="descname">ami</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.ami" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AMI used to launch the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.associate_public_ip_address">
<code class="descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the Instance is associated with a public IP address or not (Boolean).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.credit_specifications">
<code class="descname">credit_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.credit_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The credit specification of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The EBS block device mappings of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the Instance is EBS optimized or not (Boolean).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The ephemeral block device mappings of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.host_id">
<code class="descname">host_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.host_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the dedicated host the instance will be assigned to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance profile associated with the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether detailed monitoring is enabled or disabled for the Instance (Boolean).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface that was created with the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.password_data">
<code class="descname">password_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.password_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base-64 encoded encrypted password data for the instance.
Useful for getting the administrator password for instances running Microsoft Windows.
This attribute is only exported if <code class="docutils literal notranslate"><span class="pre">get_password_data</span></code> is true.
See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.placement_group">
<code class="descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The placement group of the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.private_dns">
<code class="descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the Instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address assigned to the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.public_dns">
<code class="descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the Instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the Instance, if applicable. <strong>NOTE</strong>: If you are using an <cite>``aws_eip`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/eip.html">https://www.terraform.io/docs/providers/aws/r/eip.html</a>&gt;`_ with your instance, you should refer to the EIP’s address directly and not use <code class="docutils literal notranslate"><span class="pre">public_ip</span></code>, as this field will change after the EIP is attached.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.root_block_devices">
<code class="descname">root_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.root_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The root block device mappings of the Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.source_dest_check">
<code class="descname">source_dest_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.source_dest_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the network interface performs source/destination checking (Boolean).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC subnet ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.tenancy">
<code class="descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenancy of the instance: <code class="docutils literal notranslate"><span class="pre">dedicated</span></code>, <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>SHA-1 hash of User Data supplied to the Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.user_data_base64">
<code class="descname">user_data_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.user_data_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded contents of User Data supplied to the Instance. Valid UTF-8 contents can be decoded with the <cite>``base64decode`</cite> function &lt;<a class="reference external" href="https://www.terraform.io/docs/configuration/functions/base64decode.html">https://www.terraform.io/docs/configuration/functions/base64decode.html</a>&gt;`_. This attribute is only exported if <code class="docutils literal notranslate"><span class="pre">get_user_data</span></code> is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups in a non-default VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstanceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetInstancesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetInstancesResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>instance_state_names=None</em>, <em>instance_tags=None</em>, <em>private_ips=None</em>, <em>public_ips=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstancesResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>IDs of instances found through the filter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstancesResult.private_ips">
<code class="descname">private_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstancesResult.private_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP addresses of instances found through the filter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstancesResult.public_ips">
<code class="descname">public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstancesResult.public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Public IP addresses of instances found through the filter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInstancesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetInternetGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetInternetGatewayResult</code><span class="sig-paren">(</span><em>attachments=None</em>, <em>filters=None</em>, <em>internet_gateway_id=None</em>, <em>owner_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetInternetGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInternetGateway.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInternetGatewayResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInternetGatewayResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the internet gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetInternetGatewayResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetInternetGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetLaunchConfigurationResult</code><span class="sig-paren">(</span><em>associate_public_ip_address=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>enable_monitoring=None</em>, <em>ephemeral_block_devices=None</em>, <em>iam_instance_profile=None</em>, <em>image_id=None</em>, <em>instance_type=None</em>, <em>key_name=None</em>, <em>name=None</em>, <em>placement_tenancy=None</em>, <em>root_block_devices=None</em>, <em>security_groups=None</em>, <em>spot_price=None</em>, <em>user_data=None</em>, <em>vpc_classic_link_id=None</em>, <em>vpc_classic_link_security_groups=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLaunchConfiguration.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.associate_public_ip_address">
<code class="descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether a Public IP address is associated with the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The EBS Block Devices attached to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.enable_monitoring">
<code class="descname">enable_monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.enable_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Detailed Monitoring is Enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ephemeral volumes on the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Instance Profile to associate with launched instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Image ID of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instance Type of the instance to launch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Key Name that should be used for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the launch configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.placement_tenancy">
<code class="descname">placement_tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.placement_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tenancy of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.root_block_devices">
<code class="descname">root_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.root_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The Root Block Device of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of associated Security Group IDS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.spot_price">
<code class="descname">spot_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.spot_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The Price to use for reserving Spot instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Data of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.vpc_classic_link_id">
<code class="descname">vpc_classic_link_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.vpc_classic_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a ClassicLink-enabled VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.vpc_classic_link_security_groups">
<code class="descname">vpc_classic_link_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.vpc_classic_link_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchConfigurationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetLaunchTemplateResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>block_device_mappings=None</em>, <em>credit_specifications=None</em>, <em>default_version=None</em>, <em>description=None</em>, <em>disable_api_termination=None</em>, <em>ebs_optimized=None</em>, <em>elastic_gpu_specifications=None</em>, <em>iam_instance_profiles=None</em>, <em>image_id=None</em>, <em>instance_initiated_shutdown_behavior=None</em>, <em>instance_market_options=None</em>, <em>instance_type=None</em>, <em>kernel_id=None</em>, <em>key_name=None</em>, <em>latest_version=None</em>, <em>monitorings=None</em>, <em>name=None</em>, <em>network_interfaces=None</em>, <em>placements=None</em>, <em>ram_disk_id=None</em>, <em>security_group_names=None</em>, <em>tag_specifications=None</em>, <em>tags=None</em>, <em>user_data=None</em>, <em>vpc_security_group_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLaunchTemplate.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.block_device_mappings">
<code class="descname">block_device_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.block_device_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify volumes to attach to the instance besides the volumes specified by the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.credit_specifications">
<code class="descname">credit_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.credit_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the credit specification of the instance. See Credit
Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.default_version">
<code class="descname">default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.disable_api_termination">
<code class="descname">disable_api_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.disable_api_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.elastic_gpu_specifications">
<code class="descname">elastic_gpu_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.elastic_gpu_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The elastic GPU to attach to the instance. See Elastic GPU
below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.iam_instance_profiles">
<code class="descname">iam_instance_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.iam_instance_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI from which to launch the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.instance_initiated_shutdown_behavior">
<code class="descname">instance_initiated_shutdown_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.instance_initiated_shutdown_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>Shutdown behavior for the instance. Can be <code class="docutils literal notranslate"><span class="pre">stop</span></code> or <code class="docutils literal notranslate"><span class="pre">terminate</span></code>.
(Default: <code class="docutils literal notranslate"><span class="pre">stop</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.instance_market_options">
<code class="descname">instance_market_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.instance_market_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The market (purchasing) option for the instance.
below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.kernel_id">
<code class="descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The kernel ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name to use for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.latest_version">
<code class="descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.monitorings">
<code class="descname">monitorings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.monitorings" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring option for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.placements">
<code class="descname">placements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.placements" title="Permalink to this definition">¶</a></dt>
<dd><p>The placement of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.ram_disk_id">
<code class="descname">ram_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.ram_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the RAM disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.security_group_names">
<code class="descname">security_group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group names to associate with. If you are creating Instances in a VPC, use
<code class="docutils literal notranslate"><span class="pre">vpc_security_group_ids</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.tag_specifications">
<code class="descname">tag_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.tag_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags to apply to the resources during launch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A mapping of tags to assign to the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded user data to provide when launching the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to associate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetLaunchTemplateResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetLaunchTemplateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetNatGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetNatGatewayResult</code><span class="sig-paren">(</span><em>allocation_id=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>network_interface_id=None</em>, <em>private_ip=None</em>, <em>public_ip=None</em>, <em>state=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetNatGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNatGateway.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNatGatewayResult.allocation_id">
<code class="descname">allocation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNatGatewayResult.allocation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the EIP allocated to the selected Nat Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNatGatewayResult.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNatGatewayResult.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the ENI allocated to the selected Nat Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNatGatewayResult.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNatGatewayResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private Ip address of the selected Nat Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNatGatewayResult.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNatGatewayResult.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public Ip (EIP) address of the selected Nat Gateway.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetNetworkAclsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetNetworkAclsResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkAclsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkAcls.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkAclsResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkAclsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all the network ACL ids found. This data source will fail if none are found.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkAclsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkAclsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetNetworkInterfaceResult</code><span class="sig-paren">(</span><em>associations=None</em>, <em>attachments=None</em>, <em>availability_zone=None</em>, <em>description=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>interface_type=None</em>, <em>ipv6_addresses=None</em>, <em>mac_address=None</em>, <em>owner_id=None</em>, <em>private_dns_name=None</em>, <em>private_ip=None</em>, <em>private_ips=None</em>, <em>requester_id=None</em>, <em>security_groups=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkInterface.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.associations">
<code class="descname">associations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.associations" title="Permalink to this definition">¶</a></dt>
<dd><p>The association information for an Elastic IP address (IPv4) associated with the network interface. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.interface_type">
<code class="descname">interface_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.interface_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.ipv6_addresses">
<code class="descname">ipv6_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.ipv6_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IPv6 addresses to assign to the ENI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.mac_address">
<code class="descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The MAC address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the owner of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.private_dns_name">
<code class="descname">private_dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.private_dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IPv4 address of the network interface within the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.private_ips">
<code class="descname">private_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.private_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IPv4 addresses associated with the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.requester_id">
<code class="descname">requester_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.requester_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the entity that launched the instance on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of security groups for the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Any tags assigned to the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfaceResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfaceResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetNetworkInterfacesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetNetworkInterfacesResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfacesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkInterfaces.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfacesResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfacesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all the network interface ids found. This data source will fail if none are found.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetNetworkInterfacesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetNetworkInterfacesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetRouteResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetRouteResult</code><span class="sig-paren">(</span><em>destination_cidr_block=None</em>, <em>destination_ipv6_cidr_block=None</em>, <em>egress_only_gateway_id=None</em>, <em>gateway_id=None</em>, <em>instance_id=None</em>, <em>nat_gateway_id=None</em>, <em>network_interface_id=None</em>, <em>route_table_id=None</em>, <em>transit_gateway_id=None</em>, <em>vpc_peering_connection_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetRouteResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRoute.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetRouteTableResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetRouteTableResult</code><span class="sig-paren">(</span><em>associations=None</em>, <em>filters=None</em>, <em>owner_id=None</em>, <em>route_table_id=None</em>, <em>routes=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTable.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTableResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTableResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTableResult.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTableResult.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Route Table ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTableResult.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTableResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Subnet ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetRouteTablesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetRouteTablesResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTablesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTables.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTablesResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTablesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all the route table ids found. This data source will fail if none are found.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetRouteTablesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetRouteTablesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetSecurityGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetSecurityGroupResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>description=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecurityGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSecurityGroupResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The computed ARN of the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSecurityGroupResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the security group.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetSecurityGroupsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetSecurityGroupsResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>vpc_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecurityGroups.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSecurityGroupsResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>IDs of the matches security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSecurityGroupsResult.vpc_ids">
<code class="descname">vpc_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupsResult.vpc_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC IDs of the matched security groups. The data source’s tag or filter <em>will span VPCs</em>
unless the <code class="docutils literal notranslate"><span class="pre">vpc-id</span></code> filter is also used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSecurityGroupsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSecurityGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetSubnetIdsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetSubnetIdsResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnetIds.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSubnetIdsResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetIdsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all the subnet ids found. This data source will fail if none are found.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSubnetIdsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetSubnetResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetSubnetResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>assign_ipv6_address_on_creation=None</em>, <em>availability_zone=None</em>, <em>availability_zone_id=None</em>, <em>cidr_block=None</em>, <em>default_for_az=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>ipv6_cidr_block=None</em>, <em>ipv6_cidr_block_association_id=None</em>, <em>map_public_ip_on_launch=None</em>, <em>owner_id=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnet.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSubnetResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetSubnetResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetSubnetResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the subnet.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcDhcpOptionsResult</code><span class="sig-paren">(</span><em>dhcp_options_id=None</em>, <em>domain_name=None</em>, <em>domain_name_servers=None</em>, <em>filters=None</em>, <em>netbios_name_servers=None</em>, <em>netbios_node_type=None</em>, <em>ntp_servers=None</em>, <em>owner_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcDhcpOptions.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.dhcp_options_id">
<code class="descname">dhcp_options_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.dhcp_options_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 DHCP Options ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The suffix domain name to used when resolving non Fully Qualified Domain Names. e.g. the <code class="docutils literal notranslate"><span class="pre">search</span></code> value in the <code class="docutils literal notranslate"><span class="pre">/etc/resolv.conf</span></code> file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.domain_name_servers">
<code class="descname">domain_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.domain_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of name servers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.netbios_name_servers">
<code class="descname">netbios_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.netbios_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of NETBIOS name servers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.netbios_node_type">
<code class="descname">netbios_node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.netbios_node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The NetBIOS node type (1, 2, 4, or 8). For more information about these node types, see <a class="reference external" href="http://www.ietf.org/rfc/rfc2132.txt">RFC 2132</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.ntp_servers">
<code class="descname">ntp_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.ntp_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of NTP servers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the DHCP options set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcDhcpOptionsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcDhcpOptionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcEndpointResult</code><span class="sig-paren">(</span><em>cidr_blocks=None</em>, <em>dns_entries=None</em>, <em>id=None</em>, <em>network_interface_ids=None</em>, <em>owner_id=None</em>, <em>policy=None</em>, <em>prefix_list_id=None</em>, <em>private_dns_enabled=None</em>, <em>requester_managed=None</em>, <em>route_table_ids=None</em>, <em>security_group_ids=None</em>, <em>service_name=None</em>, <em>state=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>vpc_endpoint_type=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.cidr_blocks">
<code class="descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.dns_entries">
<code class="descname">dns_entries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.dns_entries" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS entries for the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>. DNS blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.network_interface_ids">
<code class="descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VPC endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document associated with the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.prefix_list_id">
<code class="descname">prefix_list_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.prefix_list_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix list ID of the exposed AWS service. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.private_dns_enabled">
<code class="descname">private_dns_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.private_dns_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the VPC is associated with a private hosted zone - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.requester_managed">
<code class="descname">requester_managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.requester_managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the VPC Endpoint is being managed by its service - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.route_table_ids">
<code class="descname">route_table_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.route_table_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more security groups associated with the network interfaces. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointResult.vpc_endpoint_type">
<code class="descname">vpc_endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointResult.vpc_endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Endpoint type, <code class="docutils literal notranslate"><span class="pre">Gateway</span></code> or <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcEndpointServiceResult</code><span class="sig-paren">(</span><em>acceptance_required=None</em>, <em>availability_zones=None</em>, <em>base_endpoint_dns_names=None</em>, <em>manages_vpc_endpoints=None</em>, <em>owner=None</em>, <em>private_dns_name=None</em>, <em>service=None</em>, <em>service_id=None</em>, <em>service_name=None</em>, <em>service_type=None</em>, <em>tags=None</em>, <em>vpc_endpoint_policy_supported=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcEndpointService.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.acceptance_required">
<code class="descname">acceptance_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.acceptance_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zones in which the service is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.base_endpoint_dns_names">
<code class="descname">base_endpoint_dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.base_endpoint_dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS names for the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.manages_vpc_endpoints">
<code class="descname">manages_vpc_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.manages_vpc_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the service manages its VPC endpoints - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the service owner or <code class="docutils literal notranslate"><span class="pre">amazon</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.private_dns_name">
<code class="descname">private_dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.private_dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name for the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.service_id">
<code class="descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the endpoint service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.service_type">
<code class="descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service type, <code class="docutils literal notranslate"><span class="pre">Gateway</span></code> or <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.vpc_endpoint_policy_supported">
<code class="descname">vpc_endpoint_policy_supported</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.vpc_endpoint_policy_supported" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the service supports endpoint policies - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcEndpointServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcEndpointServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcPeeringConnectionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcPeeringConnectionResult</code><span class="sig-paren">(</span><em>accepter=None</em>, <em>cidr_block=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>owner_id=None</em>, <em>peer_cidr_block=None</em>, <em>peer_owner_id=None</em>, <em>peer_region=None</em>, <em>peer_vpc_id=None</em>, <em>region=None</em>, <em>requester=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcPeeringConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcPeeringConnection.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcPeeringConnectionResult.accepter">
<code class="descname">accepter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcPeeringConnectionResult.accepter" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the accepter VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcPeeringConnectionResult.requester">
<code class="descname">requester</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcPeeringConnectionResult.requester" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the requester VPC.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>cidr_block=None</em>, <em>cidr_block_associations=None</em>, <em>default=None</em>, <em>dhcp_options_id=None</em>, <em>enable_dns_hostnames=None</em>, <em>enable_dns_support=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>instance_tenancy=None</em>, <em>ipv6_association_id=None</em>, <em>ipv6_cidr_block=None</em>, <em>main_route_table_id=None</em>, <em>owner_id=None</em>, <em>state=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpc.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the association.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.enable_dns_hostnames">
<code class="descname">enable_dns_hostnames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.enable_dns_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the VPC has DNS hostname support</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.enable_dns_support">
<code class="descname">enable_dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.enable_dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the VPC has DNS support</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.instance_tenancy">
<code class="descname">instance_tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.instance_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The allowed tenancy of instances launched into the
selected VPC. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.ipv6_association_id">
<code class="descname">ipv6_association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.ipv6_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The association ID for the IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.main_route_table_id">
<code class="descname">main_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.main_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the main route table associated with this VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The State of the association.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpcsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpcsResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>ids=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpcsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcs.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcsResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all the VPC Ids found. This data source will fail if none are found.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.GetVpcsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.GetVpcsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.GetVpnGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">GetVpnGatewayResult</code><span class="sig-paren">(</span><em>amazon_side_asn=None</em>, <em>attached_vpc_id=None</em>, <em>availability_zone=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>state=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.GetVpnGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpnGateway.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2.Instance">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ami=None</em>, <em>associate_public_ip_address=None</em>, <em>availability_zone=None</em>, <em>cpu_core_count=None</em>, <em>cpu_threads_per_core=None</em>, <em>credit_specification=None</em>, <em>disable_api_termination=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>ephemeral_block_devices=None</em>, <em>get_password_data=None</em>, <em>host_id=None</em>, <em>iam_instance_profile=None</em>, <em>instance_initiated_shutdown_behavior=None</em>, <em>instance_type=None</em>, <em>ipv6_address_count=None</em>, <em>ipv6_addresses=None</em>, <em>key_name=None</em>, <em>monitoring=None</em>, <em>network_interfaces=None</em>, <em>placement_group=None</em>, <em>private_ip=None</em>, <em>root_block_device=None</em>, <em>security_groups=None</em>, <em>source_dest_check=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>tenancy=None</em>, <em>user_data=None</em>, <em>user_data_base64=None</em>, <em>volume_tags=None</em>, <em>vpc_security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EC2 instance resource. This allows instances to be created, updated,
and deleted. Instances also support <a class="reference external" href="https://www.terraform.io/docs/provisioners/index.html">provisioning</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ami</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.</li>
<li><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Associate a public ip address with an instance in a VPC.  Boolean value.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ to start the instance in.</li>
<li><strong>cpu_core_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values">CPU Cores and Threads Per CPU Core Per Instance Type</a> - specifying this option for unsupported instance types will return an error from the EC2 API.</li>
<li><strong>cpu_threads_per_core</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">Optimizing CPU Options</a> for more information.</li>
<li><strong>credit_specification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize the credit specification of the instance. See Credit Specification below for more details.</li>
<li><strong>disable_api_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If true, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  Block device configurations only apply on resource creation. See Block Devices below for details on attributes and drift detection.</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html">EBS Optimized section</a> of the AWS User Guide for more information.</li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</li>
<li><strong>get_password_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the <code class="docutils literal notranslate"><span class="pre">password_data</span></code> attribute. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</li>
<li><strong>host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.</li>
<li><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions">EC2 documentation</a>, notably <code class="docutils literal notranslate"><span class="pre">iam:PassRole</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>instance_initiated_shutdown_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shutdown behavior for the
instance. Amazon defaults this to <code class="docutils literal notranslate"><span class="pre">stop</span></code> for EBS-backed instances and
<code class="docutils literal notranslate"><span class="pre">terminate</span></code> for instance-store instances. Cannot be set on instance-store
instances. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior">Shutdown Behavior</a> for more information.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.</li>
<li><strong>ipv6_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface</li>
<li><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name of the Key Pair to use for the instance; which can be managed using the <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> resource.</li>
<li><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)</li>
<li><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.</li>
<li><strong>placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Placement Group to start the instance in.</li>
<li><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP address to associate with the
instance in a VPC.</li>
<li><strong>root_block_device</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.</li>
<li><strong>source_dest_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Subnet ID to launch in.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</li>
<li><strong>user_data_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</li>
<li><strong>volume_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the devices created by the instance at launch time.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to associate with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.ami">
<code class="descname">ami</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.ami" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI to use for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.associate_public_ip_address">
<code class="descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate a public ip address with an instance in a VPC.  Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ to start the instance in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.cpu_core_count">
<code class="descname">cpu_core_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.cpu_core_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values">CPU Cores and Threads Per CPU Core Per Instance Type</a> - specifying this option for unsupported instance types will return an error from the EC2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.cpu_threads_per_core">
<code class="descname">cpu_threads_per_core</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.cpu_threads_per_core" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">Optimizing CPU Options</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.credit_specification">
<code class="descname">credit_specification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.credit_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the credit specification of the instance. See Credit Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.disable_api_termination">
<code class="descname">disable_api_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.disable_api_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  Block device configurations only apply on resource creation. See Block Devices below for details on attributes and drift detection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html">EBS Optimized section</a> of the AWS User Guide for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.get_password_data">
<code class="descname">get_password_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.get_password_data" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the <code class="docutils literal notranslate"><span class="pre">password_data</span></code> attribute. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.host_id">
<code class="descname">host_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.host_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions">EC2 documentation</a>, notably <code class="docutils literal notranslate"><span class="pre">iam:PassRole</span></code>.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">ipv6_address_count</span></code>- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.instance_initiated_shutdown_behavior">
<code class="descname">instance_initiated_shutdown_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.instance_initiated_shutdown_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>Shutdown behavior for the
instance. Amazon defaults this to <code class="docutils literal notranslate"><span class="pre">stop</span></code> for EBS-backed instances and
<code class="docutils literal notranslate"><span class="pre">terminate</span></code> for instance-store instances. Cannot be set on instance-store
instances. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior">Shutdown Behavior</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.ipv6_addresses">
<code class="descname">ipv6_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.ipv6_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name of the Key Pair to use for the instance; which can be managed using the <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.password_data">
<code class="descname">password_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.password_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base-64 encoded encrypted password data for the instance.
Useful for getting the administrator password for instances running Microsoft Windows.
This attribute is only exported if <code class="docutils literal notranslate"><span class="pre">get_password_data</span></code> is true.
Note that this encrypted value will be stored in the state file, as with all exported attributes.
See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.placement_group">
<code class="descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The Placement Group to start the instance in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.primary_network_interface_id">
<code class="descname">primary_network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.primary_network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance’s primary network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.private_dns">
<code class="descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP address to associate with the
instance in a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.public_dns">
<code class="descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the instance, if applicable. <strong>NOTE</strong>: If you are using an <cite>``aws_eip`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/eip.html">https://www.terraform.io/docs/providers/aws/r/eip.html</a>&gt;`_ with your instance, you should refer to the EIP’s address directly and not use <code class="docutils literal notranslate"><span class="pre">public_ip</span></code>, as this field will change after the EIP is attached.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.root_block_device">
<code class="descname">root_block_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.root_block_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.source_dest_check">
<code class="descname">source_dest_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.source_dest_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Subnet ID to launch in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.tenancy">
<code class="descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.user_data_base64">
<code class="descname">user_data_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.user_data_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.volume_tags">
<code class="descname">volume_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.volume_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the devices created by the instance at launch time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Instance.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Instance.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to associate with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.InternetGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">InternetGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a VPC Internet Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID to create in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/internet_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/internet_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.InternetGateway.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the internet gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.InternetGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.InternetGateway.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID to create in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.InternetGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.InternetGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.InternetGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.KeyPair">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">KeyPair</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>key_name=None</em>, <em>key_name_prefix=None</em>, <em>public_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.KeyPair" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">EC2 key pair</a> resource. A key pair is used to control login access to EC2 instances.</p>
<p>Currently this resource requires an existing user-supplied key pair. This key pair’s public key will be registered with AWS to allow logging-in to EC2 instances.</p>
<p>When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws">AWS documentation</a>) are:</p>
<ul class="simple">
<li>OpenSSH public key format (the format in ~/.ssh/authorized_keys)</li>
<li>Base64 encoded DER format</li>
<li>SSH public key file format as specified in RFC4716</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the key pair.</li>
<li><strong>key_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">key_name</span></code>.</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key material.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/key_pair.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/key_pair.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.KeyPair.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint as specified in section 4 of RFC 4716.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.KeyPair.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the key pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.KeyPair.key_name_prefix">
<code class="descname">key_name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.key_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">key_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.KeyPair.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key material.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.KeyPair.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.KeyPair.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.KeyPair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.LaunchConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">LaunchConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>associate_public_ip_address=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>enable_monitoring=None</em>, <em>ephemeral_block_devices=None</em>, <em>iam_instance_profile=None</em>, <em>image_id=None</em>, <em>instance_type=None</em>, <em>key_name=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>placement_tenancy=None</em>, <em>root_block_device=None</em>, <em>security_groups=None</em>, <em>spot_price=None</em>, <em>user_data=None</em>, <em>user_data_base64=None</em>, <em>vpc_classic_link_id=None</em>, <em>vpc_classic_link_security_groups=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LaunchConfiguration resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Associate a public ip address with an instance in a VPC.</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</li>
<li><strong>enable_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables/disables detailed monitoring. This is enabled by default.</li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</li>
<li><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name attribute of the IAM instance profile to associate
with launched instances.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 image ID to launch.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of instance to launch.</li>
<li><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name that should be used for the instance.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>placement_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenancy of the instance. Valid values are
<code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code>, see <a class="reference external" href="http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html">AWS’s Create Launch Configuration</a>
for more details</li>
<li><strong>root_block_device</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of associated security group IDS.</li>
<li><strong>spot_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum price to use for reserving spot instances.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</li>
<li><strong>user_data_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</li>
<li><strong>vpc_classic_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. <code class="docutils literal notranslate"><span class="pre">vpc-2730681a</span></code>)</li>
<li><strong>vpc_classic_link_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. <code class="docutils literal notranslate"><span class="pre">sg-46ae3d11</span></code>).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.associate_public_ip_address">
<code class="descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate a public ip address with an instance in a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.enable_monitoring">
<code class="descname">enable_monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.enable_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables/disables detailed monitoring. This is enabled by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The name attribute of the IAM instance profile to associate
with launched instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 image ID to launch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of instance to launch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name that should be used for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.placement_tenancy">
<code class="descname">placement_tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.placement_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenancy of the instance. Valid values are
<code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code>, see <a class="reference external" href="http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html">AWS’s Create Launch Configuration</a>
for more details</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.root_block_device">
<code class="descname">root_block_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.root_block_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of associated security group IDS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.spot_price">
<code class="descname">spot_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.spot_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price to use for reserving spot instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.user_data_base64">
<code class="descname">user_data_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.user_data_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.vpc_classic_link_id">
<code class="descname">vpc_classic_link_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.vpc_classic_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. <code class="docutils literal notranslate"><span class="pre">vpc-2730681a</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchConfiguration.vpc_classic_link_security_groups">
<code class="descname">vpc_classic_link_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.vpc_classic_link_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. <code class="docutils literal notranslate"><span class="pre">sg-46ae3d11</span></code>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.LaunchConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.LaunchConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.LaunchTemplate">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">LaunchTemplate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>block_device_mappings=None</em>, <em>capacity_reservation_specification=None</em>, <em>credit_specification=None</em>, <em>description=None</em>, <em>disable_api_termination=None</em>, <em>ebs_optimized=None</em>, <em>elastic_gpu_specifications=None</em>, <em>elastic_inference_accelerator=None</em>, <em>iam_instance_profile=None</em>, <em>image_id=None</em>, <em>instance_initiated_shutdown_behavior=None</em>, <em>instance_market_options=None</em>, <em>instance_type=None</em>, <em>kernel_id=None</em>, <em>key_name=None</em>, <em>license_specifications=None</em>, <em>monitoring=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>network_interfaces=None</em>, <em>placement=None</em>, <em>ram_disk_id=None</em>, <em>security_group_names=None</em>, <em>tag_specifications=None</em>, <em>tags=None</em>, <em>user_data=None</em>, <em>vpc_security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>block_device_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.</li>
<li><strong>capacity_reservation_specification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.</li>
<li><strong>credit_specification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize the credit specification of the instance. See Credit
Specification below for more details.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the launch template.</li>
<li><strong>disable_api_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the launched EC2 instance will be EBS-optimized.</li>
<li><strong>elastic_gpu_specifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The elastic GPU to attach to the instance. See Elastic GPU
below for more details.</li>
<li><strong>elastic_inference_accelerator</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.</li>
<li><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI from which to launch the instance.</li>
<li><strong>instance_initiated_shutdown_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shutdown behavior for the instance. Can be <code class="docutils literal notranslate"><span class="pre">stop</span></code> or <code class="docutils literal notranslate"><span class="pre">terminate</span></code>.
(Default: <code class="docutils literal notranslate"><span class="pre">stop</span></code>).</li>
<li><strong>instance_market_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The market (purchasing) option for the instance. See Market Options
below for details.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the instance.</li>
<li><strong>kernel_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kernel ID.</li>
<li><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name to use for the instance.</li>
<li><strong>license_specifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of license specifications to associate with. See License Specification below for more details.</li>
<li><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The monitoring option for the instance. See Monitoring below for more details.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.</li>
<li><strong>placement</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The placement of the instance. See Placement below for more details.</li>
<li><strong>ram_disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the RAM disk.</li>
<li><strong>security_group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group names to associate with. If you are creating Instances in a VPC, use
<code class="docutils literal notranslate"><span class="pre">vpc_security_group_ids</span></code> instead.</li>
<li><strong>tag_specifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The tags to apply to the resources during launch. See Tag Specifications below for more details.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the launch template.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded user data to provide when launching the instance.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to associate with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_template.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.block_device_mappings">
<code class="descname">block_device_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.block_device_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.capacity_reservation_specification">
<code class="descname">capacity_reservation_specification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.capacity_reservation_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.credit_specification">
<code class="descname">credit_specification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.credit_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the credit specification of the instance. See Credit
Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.default_version">
<code class="descname">default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.disable_api_termination">
<code class="descname">disable_api_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.disable_api_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.elastic_gpu_specifications">
<code class="descname">elastic_gpu_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.elastic_gpu_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The elastic GPU to attach to the instance. See Elastic GPU
below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.elastic_inference_accelerator">
<code class="descname">elastic_inference_accelerator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.elastic_inference_accelerator" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI from which to launch the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.instance_initiated_shutdown_behavior">
<code class="descname">instance_initiated_shutdown_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.instance_initiated_shutdown_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>Shutdown behavior for the instance. Can be <code class="docutils literal notranslate"><span class="pre">stop</span></code> or <code class="docutils literal notranslate"><span class="pre">terminate</span></code>.
(Default: <code class="docutils literal notranslate"><span class="pre">stop</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.instance_market_options">
<code class="descname">instance_market_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.instance_market_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The market (purchasing) option for the instance. See Market Options
below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.kernel_id">
<code class="descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The kernel ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name to use for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.latest_version">
<code class="descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.license_specifications">
<code class="descname">license_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.license_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of license specifications to associate with. See License Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring option for the instance. See Monitoring below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.placement">
<code class="descname">placement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.placement" title="Permalink to this definition">¶</a></dt>
<dd><p>The placement of the instance. See Placement below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.ram_disk_id">
<code class="descname">ram_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.ram_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the RAM disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.security_group_names">
<code class="descname">security_group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.security_group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group names to associate with. If you are creating Instances in a VPC, use
<code class="docutils literal notranslate"><span class="pre">vpc_security_group_ids</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.tag_specifications">
<code class="descname">tag_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.tag_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags to apply to the resources during launch. See Tag Specifications below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the launch template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded user data to provide when launching the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.LaunchTemplate.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to associate with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.LaunchTemplate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.LaunchTemplate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.LaunchTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.MainRouteTableAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">MainRouteTableAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>route_table_id=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for managing the main routing table of a VPC.</p>
<p>On VPC creation, the AWS API always creates an initial Main Route Table. This
resource records the ID of that Route Table under <code class="docutils literal notranslate"><span class="pre">original_route_table_id</span></code>.
The “Delete” action for a <code class="docutils literal notranslate"><span class="pre">main_route_table_association</span></code> consists of resetting
this original table as the Main Route Table for the VPC. You’ll see this
additional Route Table in the AWS console; it must remain intact in order for
the <code class="docutils literal notranslate"><span class="pre">main_route_table_association</span></code> delete to work properly.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Route Table to set as the new
main route table for the target VPC</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC whose main route table should be set</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/main_route_table_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/main_route_table_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.MainRouteTableAssociation.original_route_table_id">
<code class="descname">original_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation.original_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Used internally, see <strong>Notes</strong> below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.MainRouteTableAssociation.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table to set as the new
main route table for the target VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.MainRouteTableAssociation.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC whose main route table should be set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.MainRouteTableAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.MainRouteTableAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.MainRouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NatGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NatGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocation_id=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NatGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a VPC NAT Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Allocation ID of the Elastic IP address for the gateway.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Subnet ID of the subnet in which to place the gateway.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/nat_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/nat_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.allocation_id">
<code class="descname">allocation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.allocation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Allocation ID of the Elastic IP address for the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ENI ID of the network interface created by the NAT gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address of the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address of the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Subnet ID of the subnet in which to place the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NatGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NatGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NatGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NatGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkAcl">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NetworkAcl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>egress=None</em>, <em>ingress=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NetworkAcl resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>egress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Specifies an egress rule. Parameters defined below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Specifies an ingress rule. Parameters defined below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Subnet IDs to apply the ACL to</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated VPC.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.egress">
<code class="descname">egress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.egress" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an egress rule. Parameters defined below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an ingress rule. Parameters defined below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the network ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subnet IDs to apply the ACL to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAcl.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NetworkAcl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkAcl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkAclRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NetworkAclRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cidr_block=None</em>, <em>egress=None</em>, <em>from_port=None</em>, <em>icmp_code=None</em>, <em>icmp_type=None</em>, <em>ipv6_cidr_block=None</em>, <em>network_acl_id=None</em>, <em>protocol=None</em>, <em>rule_action=None</em>, <em>rule_number=None</em>, <em>to_port=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NetworkAclRule resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).</li>
<li><strong>egress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>from_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The from port to match.</li>
<li><strong>icmp_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1</li>
<li><strong>icmp_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1</li>
<li><strong>ipv6_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 CIDR block to allow or deny.</li>
<li><strong>network_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network ACL.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol. A value of -1 means all protocols.</li>
<li><strong>rule_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether to allow or deny the traffic that matches the rule. Accepted values: <code class="docutils literal notranslate"><span class="pre">allow</span></code> | <code class="docutils literal notranslate"><span class="pre">deny</span></code></li>
<li><strong>rule_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.</li>
<li><strong>to_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The to port to match.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.egress">
<code class="descname">egress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.egress" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.from_port">
<code class="descname">from_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.from_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The from port to match.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.icmp_code">
<code class="descname">icmp_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.icmp_code" title="Permalink to this definition">¶</a></dt>
<dd><p>ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.icmp_type">
<code class="descname">icmp_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.icmp_type" title="Permalink to this definition">¶</a></dt>
<dd><p>ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 CIDR block to allow or deny.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.network_acl_id">
<code class="descname">network_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.network_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol. A value of -1 means all protocols.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.rule_action">
<code class="descname">rule_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.rule_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to allow or deny the traffic that matches the rule. Accepted values: <code class="docutils literal notranslate"><span class="pre">allow</span></code> | <code class="docutils literal notranslate"><span class="pre">deny</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.rule_number">
<code class="descname">rule_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.rule_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkAclRule.to_port">
<code class="descname">to_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.to_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The to port to match.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NetworkAclRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkAclRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkAclRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterface">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NetworkInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attachments=None</em>, <em>description=None</em>, <em>private_ip=None</em>, <em>private_ips=None</em>, <em>private_ips_count=None</em>, <em>security_groups=None</em>, <em>source_dest_check=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic network interface (ENI) resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attachments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Block to define the attachment of the ENI. Documented below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the network interface.</li>
<li><strong>private_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of private IPs to assign to the ENI.</li>
<li><strong>private_ips_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of security group IDs to assign to the ENI.</li>
<li><strong>source_dest_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable source destination checking for the ENI. Default true.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to create the ENI in.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.attachments">
<code class="descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>Block to define the attachment of the ENI. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.private_ips">
<code class="descname">private_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.private_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of private IPs to assign to the ENI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.private_ips_count">
<code class="descname">private_ips_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.private_ips_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of security group IDs to assign to the ENI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.source_dest_check">
<code class="descname">source_dest_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.source_dest_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable source destination checking for the ENI. Default true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet ID to create the ENI in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterface.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NetworkInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NetworkInterfaceAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_index=None</em>, <em>instance_id=None</em>, <em>network_interface_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attach an Elastic network interface (ENI) resource with EC2 instance.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>device_index</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Network interface index (int).</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance ID to attach.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ENI ID to attach.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.attachment_id">
<code class="descname">attachment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ENI Attachment ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.device_index">
<code class="descname">device_index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.device_index" title="Permalink to this definition">¶</a></dt>
<dd><p>Network interface index (int).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance ID to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ENI ID to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Network Interface Attachment.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterfaceAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">NetworkInterfaceSecurityGroupAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>network_interface_id=None</em>, <em>security_group_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NetworkInterfaceSecurityGroupAttachment resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network interface to attach to.</li>
<li><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface_sg_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_interface_sg_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface to attach to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.NetworkInterfaceSecurityGroupAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.PeeringConnectionOptions">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">PeeringConnectionOptions</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accepter=None</em>, <em>requester=None</em>, <em>vpc_peering_connection_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PeeringConnectionOptions resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>accepter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that accepts
the peering connection (a maximum of one).</li>
<li><strong>requester</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that requests
the peering connection (a maximum of one).</li>
<li><strong>vpc_peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the requester VPC peering connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection_options.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection_options.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.PeeringConnectionOptions.accepter">
<code class="descname">accepter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions.accepter" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that accepts
the peering connection (a maximum of one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.PeeringConnectionOptions.requester">
<code class="descname">requester</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions.requester" title="Permalink to this definition">¶</a></dt>
<dd><p>A optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that requests
the peering connection (a maximum of one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.PeeringConnectionOptions.vpc_peering_connection_id">
<code class="descname">vpc_peering_connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions.vpc_peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the requester VPC peering connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.PeeringConnectionOptions.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.PeeringConnectionOptions.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PeeringConnectionOptions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.PlacementGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">PlacementGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>strategy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PlacementGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EC2 placement group. Read more about placement groups
in <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">AWS Docs</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the placement group.</li>
<li><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The placement strategy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/placement_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/placement_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.PlacementGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.PlacementGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the placement group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.PlacementGroup.strategy">
<code class="descname">strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.PlacementGroup.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The placement strategy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.PlacementGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PlacementGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.PlacementGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.PlacementGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.ProxyProtocolPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">ProxyProtocolPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance_ports=None</em>, <em>load_balancer=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.ProxyProtocolPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a proxy protocol policy, which allows an ELB to carry a client connection information to a backend.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.</li>
<li><strong>load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancer to which the policy
should be attached.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/proxy_protocol_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/proxy_protocol_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.ProxyProtocolPolicy.instance_ports">
<code class="descname">instance_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.ProxyProtocolPolicy.instance_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.ProxyProtocolPolicy.load_balancer">
<code class="descname">load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.ProxyProtocolPolicy.load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancer to which the policy
should be attached.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.ProxyProtocolPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.ProxyProtocolPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.ProxyProtocolPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.ProxyProtocolPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Route">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_cidr_block=None</em>, <em>destination_ipv6_cidr_block=None</em>, <em>egress_only_gateway_id=None</em>, <em>gateway_id=None</em>, <em>instance_id=None</em>, <em>nat_gateway_id=None</em>, <em>network_interface_id=None</em>, <em>route_table_id=None</em>, <em>transit_gateway_id=None</em>, <em>vpc_peering_connection_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Route resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destination_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block.</li>
<li><strong>destination_ipv6_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination IPv6 CIDR block.</li>
<li><strong>egress_only_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of a VPC Egress Only Internet Gateway.</li>
<li><strong>gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of a VPC internet gateway or a virtual private gateway.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of an EC2 instance.</li>
<li><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of a VPC NAT gateway.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of an EC2 network interface.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the routing table.</li>
<li><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of an EC2 Transit Gateway.</li>
<li><strong>vpc_peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of a VPC peering connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.destination_cidr_block">
<code class="descname">destination_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.destination_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.destination_ipv6_cidr_block">
<code class="descname">destination_ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.destination_ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.egress_only_gateway_id">
<code class="descname">egress_only_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.egress_only_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of a VPC Egress Only Internet Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.gateway_id">
<code class="descname">gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of a VPC internet gateway or a virtual private gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of an EC2 instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.nat_gateway_id">
<code class="descname">nat_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of a VPC NAT gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of an EC2 network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the routing table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of an EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Route.vpc_peering_connection_id">
<code class="descname">vpc_peering_connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Route.vpc_peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of a VPC peering connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.RouteTable">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">RouteTable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>propagating_vgws=None</em>, <em>routes=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RouteTable resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>propagating_vgws</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual gateways for propagation.</li>
<li><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of route objects. Their keys are documented below. This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route_table.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTable.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTable.propagating_vgws">
<code class="descname">propagating_vgws</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.propagating_vgws" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of virtual gateways for propagation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTable.routes">
<code class="descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of route objects. Their keys are documented below. This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTable.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTable.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.RouteTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.RouteTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.RouteTableAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">RouteTableAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>route_table_id=None</em>, <em>subnet_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create an association between a subnet and routing table.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the routing table to associate with.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet ID to create an association.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route_table_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route_table_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTableAssociation.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTableAssociation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the routing table to associate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.RouteTableAssociation.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.RouteTableAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnet ID to create an association.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.RouteTableAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.RouteTableAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.RouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SecurityGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>egress=None</em>, <em>ingress=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>revoke_rules_on_delete=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityGroup resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>egress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</li>
<li><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/security_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the security group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.egress">
<code class="descname">egress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.egress" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.ingress">
<code class="descname">ingress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroup.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SecurityGroupRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SecurityGroupRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cidr_blocks=None</em>, <em>description=None</em>, <em>from_port=None</em>, <em>ipv6_cidr_blocks=None</em>, <em>prefix_list_ids=None</em>, <em>protocol=None</em>, <em>security_group_id=None</em>, <em>self=None</em>, <em>source_security_group_id=None</em>, <em>to_port=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityGroupRule resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cidr_blocks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">source_security_group_id</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule.</li>
<li><strong>from_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The start port (or ICMP type number if protocol is “icmp”).</li>
<li><strong>ipv6_cidr_blocks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IPv6 CIDR blocks.</li>
<li><strong>prefix_list_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of prefix list IDs (for allowing access to VPC endpoints).
Only valid with <code class="docutils literal notranslate"><span class="pre">egress</span></code>.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol. If not icmp, tcp, udp, or all use the <a class="reference external" href="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">protocol number</a></li>
<li><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group to apply this rule to.</li>
<li><strong>self</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the security group itself will be added as
a source to this ingress rule.</li>
<li><strong>source_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group id to allow access to/from,
depending on the <code class="docutils literal notranslate"><span class="pre">type</span></code>. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code>.</li>
<li><strong>to_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The end port (or ICMP code if protocol is “icmp”).</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of rule being created. Valid options are <code class="docutils literal notranslate"><span class="pre">ingress</span></code> (inbound)
or <code class="docutils literal notranslate"><span class="pre">egress</span></code> (outbound).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/security_group_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/security_group_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.cidr_blocks">
<code class="descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">source_security_group_id</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.from_port">
<code class="descname">from_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.from_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The start port (or ICMP type number if protocol is “icmp”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.ipv6_cidr_blocks">
<code class="descname">ipv6_cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.ipv6_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IPv6 CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.prefix_list_ids">
<code class="descname">prefix_list_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.prefix_list_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of prefix list IDs (for allowing access to VPC endpoints).
Only valid with <code class="docutils literal notranslate"><span class="pre">egress</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol. If not icmp, tcp, udp, or all use the <a class="reference external" href="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">protocol number</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group to apply this rule to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.self">
<code class="descname">self</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.self" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the security group itself will be added as
a source to this ingress rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.source_security_group_id">
<code class="descname">source_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.source_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group id to allow access to/from,
depending on the <code class="docutils literal notranslate"><span class="pre">type</span></code>. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.to_port">
<code class="descname">to_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.to_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The end port (or ICMP code if protocol is “icmp”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SecurityGroupRule.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of rule being created. Valid options are <code class="docutils literal notranslate"><span class="pre">ingress</span></code> (inbound)
or <code class="docutils literal notranslate"><span class="pre">egress</span></code> (outbound).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SecurityGroupRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SecurityGroupRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SecurityGroupRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SnapshotCreateVolumePermission">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SnapshotCreateVolumePermission</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>snapshot_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SnapshotCreateVolumePermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds permission to create volumes off of a given EBS Snapshot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An AWS Account ID to add create volume permissions</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot ID</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/snapshot_create_volume_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/snapshot_create_volume_permission.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SnapshotCreateVolumePermission.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SnapshotCreateVolumePermission.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An AWS Account ID to add create volume permissions</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SnapshotCreateVolumePermission.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SnapshotCreateVolumePermission.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A snapshot ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SnapshotCreateVolumePermission.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SnapshotCreateVolumePermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SnapshotCreateVolumePermission.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SnapshotCreateVolumePermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotDatafeedSubscription">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SpotDatafeedSubscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>prefix=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotDatafeedSubscription" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Note:</strong> There is only a single subscription allowed per account.</div></blockquote>
<p>To help you understand the charges for your Spot instances, Amazon EC2 provides a data feed that describes your Spot instance usage and pricing.
This data feed is sent to an Amazon S3 bucket that you specify when you subscribe to the data feed.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which to store the Spot instance data feed.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path of folder inside bucket to place spot pricing data.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_datafeed_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_datafeed_subscription.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotDatafeedSubscription.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotDatafeedSubscription.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 bucket in which to store the Spot instance data feed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotDatafeedSubscription.prefix">
<code class="descname">prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotDatafeedSubscription.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Path of folder inside bucket to place spot pricing data.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SpotDatafeedSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotDatafeedSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotDatafeedSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotDatafeedSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotFleetRequest">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SpotFleetRequest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocation_strategy=None</em>, <em>excess_capacity_termination_policy=None</em>, <em>fleet_type=None</em>, <em>iam_fleet_role=None</em>, <em>instance_interruption_behaviour=None</em>, <em>instance_pools_to_use_count=None</em>, <em>launch_specifications=None</em>, <em>load_balancers=None</em>, <em>replace_unhealthy_instances=None</em>, <em>spot_price=None</em>, <em>target_capacity=None</em>, <em>target_group_arns=None</em>, <em>terminate_instances_with_expiration=None</em>, <em>valid_from=None</em>, <em>valid_until=None</em>, <em>wait_for_fulfillment=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an EC2 Spot Fleet Request resource. This allows a fleet of Spot
instances to be requested on the Spot market.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocation_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
<code class="docutils literal notranslate"><span class="pre">lowestPrice</span></code>.</li>
<li><strong>excess_capacity_termination_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.</li>
<li><strong>fleet_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is <code class="docutils literal notranslate"><span class="pre">maintain</span></code>.</li>
<li><strong>iam_fleet_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.</li>
<li><strong>instance_interruption_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
<code class="docutils literal notranslate"><span class="pre">terminate</span></code>.</li>
<li><strong>instance_pools_to_use_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Spot pools across which to allocate your target Spot capacity.
Valid only when <code class="docutils literal notranslate"><span class="pre">allocation_strategy</span></code> is set to <code class="docutils literal notranslate"><span class="pre">lowestPrice</span></code>. Spot Fleet selects
the cheapest Spot pools and evenly allocates your target Spot capacity across
the number of Spot pools that you specify.</li>
<li><strong>launch_specifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Used to define the launch configuration of the
spot-fleet request. Can be specified multiple times to define different bids
across different markets and instance types.</li>
<li><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of elastic load balancer names to add to the Spot fleet.</li>
<li><strong>replace_unhealthy_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Spot fleet should replace unhealthy instances. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>spot_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum bid price per unit hour.</li>
<li><strong>target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.</li>
<li><strong>target_group_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">aws_alb_target_group</span></code> ARNs, for use with Application Load Balancing.</li>
<li><strong>terminate_instances_with_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.</li>
<li><strong>valid_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.</li>
<li><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The end date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_fleet_request.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_fleet_request.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.allocation_strategy">
<code class="descname">allocation_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.allocation_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
<code class="docutils literal notranslate"><span class="pre">lowestPrice</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.excess_capacity_termination_policy">
<code class="descname">excess_capacity_termination_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.excess_capacity_termination_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.fleet_type">
<code class="descname">fleet_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.fleet_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is <code class="docutils literal notranslate"><span class="pre">maintain</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.iam_fleet_role">
<code class="descname">iam_fleet_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.iam_fleet_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.instance_interruption_behaviour">
<code class="descname">instance_interruption_behaviour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.instance_interruption_behaviour" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
<code class="docutils literal notranslate"><span class="pre">terminate</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.instance_pools_to_use_count">
<code class="descname">instance_pools_to_use_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.instance_pools_to_use_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Spot pools across which to allocate your target Spot capacity.
Valid only when <code class="docutils literal notranslate"><span class="pre">allocation_strategy</span></code> is set to <code class="docutils literal notranslate"><span class="pre">lowestPrice</span></code>. Spot Fleet selects
the cheapest Spot pools and evenly allocates your target Spot capacity across
the number of Spot pools that you specify.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.launch_specifications">
<code class="descname">launch_specifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.launch_specifications" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to define the launch configuration of the
spot-fleet request. Can be specified multiple times to define different bids
across different markets and instance types.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.load_balancers">
<code class="descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of elastic load balancer names to add to the Spot fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.replace_unhealthy_instances">
<code class="descname">replace_unhealthy_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.replace_unhealthy_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Spot fleet should replace unhealthy instances. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.spot_price">
<code class="descname">spot_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.spot_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum bid price per unit hour.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.spot_request_state">
<code class="descname">spot_request_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.spot_request_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the Spot fleet request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.target_capacity">
<code class="descname">target_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.target_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.target_group_arns">
<code class="descname">target_group_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.target_group_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">aws_alb_target_group</span></code> ARNs, for use with Application Load Balancing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.terminate_instances_with_expiration">
<code class="descname">terminate_instances_with_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.terminate_instances_with_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.valid_from">
<code class="descname">valid_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.valid_from" title="Permalink to this definition">¶</a></dt>
<dd><p>The start date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotFleetRequest.valid_until">
<code class="descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>The end date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SpotFleetRequest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotFleetRequest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotFleetRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotInstanceRequest">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">SpotInstanceRequest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ami=None</em>, <em>associate_public_ip_address=None</em>, <em>availability_zone=None</em>, <em>block_duration_minutes=None</em>, <em>cpu_core_count=None</em>, <em>cpu_threads_per_core=None</em>, <em>credit_specification=None</em>, <em>disable_api_termination=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>ephemeral_block_devices=None</em>, <em>get_password_data=None</em>, <em>host_id=None</em>, <em>iam_instance_profile=None</em>, <em>instance_initiated_shutdown_behavior=None</em>, <em>instance_interruption_behaviour=None</em>, <em>instance_type=None</em>, <em>ipv6_address_count=None</em>, <em>ipv6_addresses=None</em>, <em>key_name=None</em>, <em>launch_group=None</em>, <em>monitoring=None</em>, <em>network_interfaces=None</em>, <em>placement_group=None</em>, <em>private_ip=None</em>, <em>root_block_device=None</em>, <em>security_groups=None</em>, <em>source_dest_check=None</em>, <em>spot_price=None</em>, <em>spot_type=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>tenancy=None</em>, <em>user_data=None</em>, <em>user_data_base64=None</em>, <em>valid_from=None</em>, <em>valid_until=None</em>, <em>volume_tags=None</em>, <em>vpc_security_group_ids=None</em>, <em>wait_for_fulfillment=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SpotInstanceRequest resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ami</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.</li>
<li><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Associate a public ip address with an instance in a VPC.  Boolean value.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ to start the instance in.</li>
<li><strong>block_duration_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
Note that you can’t specify an Availability Zone group or a launch group if you specify a duration.</li>
<li><strong>cpu_core_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values">CPU Cores and Threads Per CPU Core Per Instance Type</a> - specifying this option for unsupported instance types will return an error from the EC2 API.</p>
</li>
<li><strong>cpu_threads_per_core</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">Optimizing CPU Options</a> for more information.</p>
</li>
<li><strong>credit_specification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize the credit specification of the instance. See Credit Specification below for more details.</li>
<li><strong>disable_api_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If true, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</li>
<li><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  Block device configurations only apply on resource creation. See Block Devices below for details on attributes and drift detection.</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html">EBS Optimized section</a> of the AWS User Guide for more information.</p>
</li>
<li><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</li>
<li><strong>get_password_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the <code class="docutils literal notranslate"><span class="pre">password_data</span></code> attribute. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</li>
<li><strong>host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.</li>
<li><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions">EC2 documentation</a>, notably <code class="docutils literal notranslate"><span class="pre">iam:PassRole</span></code>.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>instance_initiated_shutdown_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Shutdown behavior for the
instance. Amazon defaults this to <code class="docutils literal notranslate"><span class="pre">stop</span></code> for EBS-backed instances and
<code class="docutils literal notranslate"><span class="pre">terminate</span></code> for instance-store instances. Cannot be set on instance-store
instances. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior">Shutdown Behavior</a> for more information.</p>
</li>
<li><strong>instance_interruption_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a Spot instance stops or terminates when it is interrupted. Default is <code class="docutils literal notranslate"><span class="pre">terminate</span></code> as this is the current AWS behaviour.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.</li>
<li><strong>ipv6_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface</li>
<li><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name of the Key Pair to use for the instance; which can be managed using the <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> resource.</li>
<li><strong>launch_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A launch group is a group of spot instances that launch together and terminate together.
If left empty instances are launched and terminated individually.</li>
<li><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)</li>
<li><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.</li>
<li><strong>placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Placement Group to start the instance in.</li>
<li><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP address to associate with the
instance in a VPC.</li>
<li><strong>root_block_device</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.</li>
<li><strong>source_dest_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.</li>
<li><strong>spot_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum price to request on the spot market.</li>
<li><strong>spot_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">one-time</span></code>, after
the instance is terminated, the spot request will be closed.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Subnet ID to launch in.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</li>
<li><strong>user_data_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</li>
<li><strong>valid_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The start date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.</p>
</li>
<li><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The end date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. The default end date is 7 days from the current date.</p>
</li>
<li><strong>volume_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the devices created by the instance at launch time.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to associate with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_instance_request.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/spot_instance_request.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.ami">
<code class="descname">ami</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.ami" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI to use for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.associate_public_ip_address">
<code class="descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate a public ip address with an instance in a VPC.  Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ to start the instance in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.block_duration_minutes">
<code class="descname">block_duration_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.block_duration_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
Note that you can’t specify an Availability Zone group or a launch group if you specify a duration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.cpu_core_count">
<code class="descname">cpu_core_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.cpu_core_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the number of CPU cores for an instance. This option is
only supported on creation of instance type that support CPU Options
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values">CPU Cores and Threads Per CPU Core Per Instance Type</a> - specifying this option for unsupported instance types will return an error from the EC2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.cpu_threads_per_core">
<code class="descname">cpu_threads_per_core</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.cpu_threads_per_core" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">Optimizing CPU Options</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.credit_specification">
<code class="descname">credit_specification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.credit_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the credit specification of the instance. See Credit Specification below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.disable_api_termination">
<code class="descname">disable_api_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.disable_api_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, enables <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination">EC2 Instance
Termination Protection</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  Block device configurations only apply on resource creation. See Block Devices below for details on attributes and drift detection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.
Note that if this is not set on an instance type that is optimized by default then
this will show as disabled but if the instance type is optimized by default then
there is no need to set this and there is no effect to disabling it.
See the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html">EBS Optimized section</a> of the AWS User Guide for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.get_password_data">
<code class="descname">get_password_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.get_password_data" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the <code class="docutils literal notranslate"><span class="pre">password_data</span></code> attribute. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html">GetPasswordData</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.host_id">
<code class="descname">host_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.host_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.iam_instance_profile">
<code class="descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Instance Profile to
launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions">EC2 documentation</a>, notably <code class="docutils literal notranslate"><span class="pre">iam:PassRole</span></code>.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">ipv6_address_count</span></code>- (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.instance_initiated_shutdown_behavior">
<code class="descname">instance_initiated_shutdown_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.instance_initiated_shutdown_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>Shutdown behavior for the
instance. Amazon defaults this to <code class="docutils literal notranslate"><span class="pre">stop</span></code> for EBS-backed instances and
<code class="docutils literal notranslate"><span class="pre">terminate</span></code> for instance-store instances. Cannot be set on instance-store
instances. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior">Shutdown Behavior</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.instance_interruption_behaviour">
<code class="descname">instance_interruption_behaviour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.instance_interruption_behaviour" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a Spot instance stops or terminates when it is interrupted. Default is <code class="docutils literal notranslate"><span class="pre">terminate</span></code> as this is the current AWS behaviour.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.ipv6_addresses">
<code class="descname">ipv6_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.ipv6_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.key_name">
<code class="descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name of the Key Pair to use for the instance; which can be managed using the <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.launch_group">
<code class="descname">launch_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.launch_group" title="Permalink to this definition">¶</a></dt>
<dd><p>A launch group is a group of spot instances that launch together and terminate together.
If left empty instances are launched and terminated individually.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.monitoring">
<code class="descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize network interfaces to be attached at instance boot time. See Network Interfaces below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.placement_group">
<code class="descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The Placement Group to start the instance in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.private_dns">
<code class="descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP address to associate with the
instance in a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.public_dns">
<code class="descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the instance, if applicable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.root_block_device">
<code class="descname">root_block_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.root_block_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.source_dest_check">
<code class="descname">source_dest_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.source_dest_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if traffic is routed to the instance when
the destination address does not match the instance. Used for NAT or VPNs. Defaults true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.spot_bid_status">
<code class="descname">spot_bid_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.spot_bid_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html">bid
status</a>
of the Spot Instance Request.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">spot_request_state</span></code> The current <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#creating-spot-request-status">request
state</a>
of the Spot Instance Request.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.spot_instance_id">
<code class="descname">spot_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.spot_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instance ID (if any) that is currently fulfilling
the Spot Instance request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.spot_price">
<code class="descname">spot_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.spot_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price to request on the spot market.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.spot_type">
<code class="descname">spot_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.spot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">one-time</span></code>, after
the instance is terminated, the spot request will be closed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Subnet ID to launch in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.tenancy">
<code class="descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see <code class="docutils literal notranslate"><span class="pre">user_data_base64</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.user_data_base64">
<code class="descname">user_data_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.user_data_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be used instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> to pass base64-encoded binary data directly. Use this instead of <code class="docutils literal notranslate"><span class="pre">user_data</span></code> whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.valid_from">
<code class="descname">valid_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.valid_from" title="Permalink to this definition">¶</a></dt>
<dd><p>The start date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.valid_until">
<code class="descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>The end date and time of the request, in UTC <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339</a> format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. The default end date is 7 days from the current date.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.volume_tags">
<code class="descname">volume_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.volume_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the devices created by the instance at launch time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to associate with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.SpotInstanceRequest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.SpotInstanceRequest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.SpotInstanceRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Subnet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Subnet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>assign_ipv6_address_on_creation=None</em>, <em>availability_zone=None</em>, <em>availability_zone_id=None</em>, <em>cidr_block=None</em>, <em>ipv6_cidr_block=None</em>, <em>map_public_ip_on_launch=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an VPC subnet resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>assign_ipv6_address_on_creation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to indicate
that network interfaces created in the specified subnet should be
assigned an IPv6 address. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ for the subnet.</li>
<li><strong>availability_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AZ ID of the subnet.</li>
<li><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the subnet.</li>
<li><strong>ipv6_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 network range for the subnet,
in CIDR notation. The subnet size must use a /64 prefix length.</li>
<li><strong>map_public_ip_on_launch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/subnet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/subnet.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.assign_ipv6_address_on_creation">
<code class="descname">assign_ipv6_address_on_creation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.assign_ipv6_address_on_creation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify true to indicate
that network interfaces created in the specified subnet should be
assigned an IPv6 address. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.availability_zone_id">
<code class="descname">availability_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.availability_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZ ID of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 network range for the subnet,
in CIDR notation. The subnet size must use a /64 prefix length.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.ipv6_cidr_block_association_id">
<code class="descname">ipv6_cidr_block_association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.ipv6_cidr_block_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The association ID for the IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.map_public_ip_on_launch">
<code class="descname">map_public_ip_on_launch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.map_public_ip_on_launch" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Subnet.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Subnet.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Subnet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Subnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Subnet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Subnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VolumeAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VolumeAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_name=None</em>, <em>force_detach=None</em>, <em>instance_id=None</em>, <em>skip_destroy=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VolumeAttachment resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>device_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name to expose to the instance (for
example, <code class="docutils literal notranslate"><span class="pre">/dev/sdh</span></code> or <code class="docutils literal notranslate"><span class="pre">xvdh</span></code>).  See [Device Naming on Linux Instances][1] and [Device Naming on Windows Instances][2] for more information.</li>
<li><strong>force_detach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in <strong>data loss</strong>. See
[Detaching an Amazon EBS Volume from an Instance][3] for more information.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Instance to attach to</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Volume to be attached</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/volume_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/volume_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VolumeAttachment.device_name">
<code class="descname">device_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name to expose to the instance (for
example, <code class="docutils literal notranslate"><span class="pre">/dev/sdh</span></code> or <code class="docutils literal notranslate"><span class="pre">xvdh</span></code>).  See [Device Naming on Linux Instances][1] and [Device Naming on Windows Instances][2] for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VolumeAttachment.force_detach">
<code class="descname">force_detach</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.force_detach" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to force the
volume to detach. Useful if previous attempts failed, but use this option only
as a last resort, as this can result in <strong>data loss</strong>. See
[Detaching an Amazon EBS Volume from an Instance][3] for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VolumeAttachment.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Instance to attach to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VolumeAttachment.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Volume to be attached</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VolumeAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VolumeAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Vpc">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">Vpc</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>assign_generated_ipv6_cidr_block=None</em>, <em>cidr_block=None</em>, <em>enable_classiclink=None</em>, <em>enable_classiclink_dns_support=None</em>, <em>enable_dns_hostnames=None</em>, <em>enable_dns_support=None</em>, <em>instance_tenancy=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a VPC resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>assign_generated_ipv6_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the VPC.</li>
<li><strong>enable_classiclink</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.</li>
<li><strong>enable_classiclink_dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.</li>
<li><strong>enable_dns_hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.</li>
<li><strong>enable_dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag to enable/disable DNS support in the VPC. Defaults true.</li>
<li><strong>instance_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A tenancy option for instances launched into the VPC</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.assign_generated_ipv6_cidr_block">
<code class="descname">assign_generated_ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.assign_generated_ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.default_network_acl_id">
<code class="descname">default_network_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.default_network_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network ACL created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.default_route_table_id">
<code class="descname">default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the route table created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.default_security_group_id">
<code class="descname">default_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.default_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group created by default on VPC creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.enable_classiclink">
<code class="descname">enable_classiclink</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.enable_classiclink" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.enable_classiclink_dns_support">
<code class="descname">enable_classiclink_dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.enable_classiclink_dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.enable_dns_hostnames">
<code class="descname">enable_dns_hostnames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.enable_dns_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.enable_dns_support">
<code class="descname">enable_dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.enable_dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag to enable/disable DNS support in the VPC. Defaults true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.instance_tenancy">
<code class="descname">instance_tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.instance_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>A tenancy option for instances launched into the VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.ipv6_association_id">
<code class="descname">ipv6_association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.ipv6_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The association ID for the IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.ipv6_cidr_block">
<code class="descname">ipv6_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.ipv6_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.main_route_table_id">
<code class="descname">main_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.main_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the main route table associated with
this VPC. Note that you can change a VPC’s main route table by using an
<cite>``aws_main_route_table_association`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html">https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.Vpc.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.Vpc.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.Vpc.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Vpc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.Vpc.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.Vpc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcDhcpOptions">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcDhcpOptions</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain_name=None</em>, <em>domain_name_servers=None</em>, <em>netbios_name_servers=None</em>, <em>netbios_node_type=None</em>, <em>ntp_servers=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a VPC DHCP Options resource.</p>
<ul class="simple">
<li>Notice that all arguments are optional but you have to specify at least one argument.</li>
<li><code class="docutils literal notranslate"><span class="pre">domain_name_servers</span></code>, <code class="docutils literal notranslate"><span class="pre">netbios_name_servers</span></code>, <code class="docutils literal notranslate"><span class="pre">ntp_servers</span></code> are limited by AWS to maximum four servers only.</li>
<li>To actually use the DHCP Options Set you need to associate it to a VPC using <cite>``aws_vpc_dhcp_options_association`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/vpc_dhcp_options_association.html">https://www.terraform.io/docs/providers/aws/r/vpc_dhcp_options_association.html</a>&gt;`_.</li>
<li>If you delete a DHCP Options Set, all VPCs using it will be associated to AWS’s <code class="docutils literal notranslate"><span class="pre">default</span></code> DHCP Option Set.</li>
<li>In most cases unless you’re configuring your own DNS you’ll want to set <code class="docutils literal notranslate"><span class="pre">domain_name_servers</span></code> to <code class="docutils literal notranslate"><span class="pre">AmazonProvidedDNS</span></code>.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the <code class="docutils literal notranslate"><span class="pre">search</span></code> value in the <code class="docutils literal notranslate"><span class="pre">/etc/resolv.conf</span></code> file.</li>
<li><strong>domain_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of name servers to configure in <code class="docutils literal notranslate"><span class="pre">/etc/resolv.conf</span></code>. If you want to use the default AWS nameservers you should set this to <code class="docutils literal notranslate"><span class="pre">AmazonProvidedDNS</span></code>.</li>
<li><strong>netbios_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of NETBIOS name servers.</li>
<li><strong>netbios_node_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see <a class="reference external" href="http://www.ietf.org/rfc/rfc2132.txt">RFC 2132</a>.</p>
</li>
<li><strong>ntp_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of NTP servers to configure.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_dhcp_options.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_dhcp_options.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the <code class="docutils literal notranslate"><span class="pre">search</span></code> value in the <code class="docutils literal notranslate"><span class="pre">/etc/resolv.conf</span></code> file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.domain_name_servers">
<code class="descname">domain_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.domain_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of name servers to configure in <code class="docutils literal notranslate"><span class="pre">/etc/resolv.conf</span></code>. If you want to use the default AWS nameservers you should set this to <code class="docutils literal notranslate"><span class="pre">AmazonProvidedDNS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.netbios_name_servers">
<code class="descname">netbios_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.netbios_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of NETBIOS name servers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.netbios_node_type">
<code class="descname">netbios_node_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.netbios_node_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see <a class="reference external" href="http://www.ietf.org/rfc/rfc2132.txt">RFC 2132</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.ntp_servers">
<code class="descname">ntp_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.ntp_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of NTP servers to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the DHCP options set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcDhcpOptions.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcDhcpOptions.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcDhcpOptionsAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcDhcpOptionsAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dhcp_options_id=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptionsAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a VPC DHCP Options Association resource.</p>
<ul class="simple">
<li>You can only associate one DHCP Options Set to a given VPC ID.</li>
<li>Removing the DHCP Options Association automatically sets AWS’s <code class="docutils literal notranslate"><span class="pre">default</span></code> DHCP Options Set to the VPC.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dhcp_options_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the DHCP Options Set to associate to the VPC.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC to which we would like to associate a DHCP Options Set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_dhcp_options_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_dhcp_options_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptionsAssociation.dhcp_options_id">
<code class="descname">dhcp_options_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptionsAssociation.dhcp_options_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the DHCP Options Set to associate to the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcDhcpOptionsAssociation.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptionsAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC to which we would like to associate a DHCP Options Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcDhcpOptionsAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptionsAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcDhcpOptionsAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcDhcpOptionsAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpoint">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpoint</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_accept=None</em>, <em>policy=None</em>, <em>private_dns_enabled=None</em>, <em>route_table_ids=None</em>, <em>security_group_ids=None</em>, <em>service_name=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>vpc_endpoint_type=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcEndpoint resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_accept</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).</li>
<li><strong>private_dns_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>route_table_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more route table IDs. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</li>
<li><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of one or more security groups to associate with the network interface. Required for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</li>
<li><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service name, in the form <code class="docutils literal notranslate"><span class="pre">com.amazonaws.region.service</span></code> for AWS services.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC endpoint type, <code class="docutils literal notranslate"><span class="pre">Gateway</span></code> or <code class="docutils literal notranslate"><span class="pre">Interface</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC in which the endpoint will be used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.auto_accept">
<code class="descname">auto_accept</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.auto_accept" title="Permalink to this definition">¶</a></dt>
<dd><p>Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.cidr_blocks">
<code class="descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.dns_entries">
<code class="descname">dns_entries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.dns_entries" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS entries for the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>. DNS blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.network_interface_ids">
<code class="descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VPC endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.prefix_list_id">
<code class="descname">prefix_list_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.prefix_list_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix list ID of the exposed AWS service. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.private_dns_enabled">
<code class="descname">private_dns_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.private_dns_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.requester_managed">
<code class="descname">requester_managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.requester_managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the VPC Endpoint is being managed by its service - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.route_table_ids">
<code class="descname">route_table_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.route_table_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more route table IDs. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of one or more security groups to associate with the network interface. Required for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service name, in the form <code class="docutils literal notranslate"><span class="pre">com.amazonaws.region.service</span></code> for AWS services.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the VPC endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.vpc_endpoint_type">
<code class="descname">vpc_endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.vpc_endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC endpoint type, <code class="docutils literal notranslate"><span class="pre">Gateway</span></code> or <code class="docutils literal notranslate"><span class="pre">Interface</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Gateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpoint.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC in which the endpoint will be used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpointConnectionNotification</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>connection_events=None</em>, <em>connection_notification_arn=None</em>, <em>vpc_endpoint_id=None</em>, <em>vpc_endpoint_service_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a VPC Endpoint connection notification resource.
Connection notifications notify subscribers of VPC Endpoint events.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>connection_events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more endpoint <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters">events</a> for which to receive notifications.</li>
<li><strong>connection_notification_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic for the notifications.</li>
<li><strong>vpc_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC Endpoint to receive notifications for.</li>
<li><strong>vpc_endpoint_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC Endpoint Service to receive notifications for.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_connection_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_connection_notification.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.connection_events">
<code class="descname">connection_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.connection_events" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more endpoint <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters">events</a> for which to receive notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.connection_notification_arn">
<code class="descname">connection_notification_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.connection_notification_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic for the notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.notification_type">
<code class="descname">notification_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.notification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of notification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the notification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.vpc_endpoint_id">
<code class="descname">vpc_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.vpc_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC Endpoint to receive notifications for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.vpc_endpoint_service_id">
<code class="descname">vpc_endpoint_service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.vpc_endpoint_service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC Endpoint Service to receive notifications for.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointConnectionNotification.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointConnectionNotification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointRouteTableAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpointRouteTableAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>route_table_id=None</em>, <em>vpc_endpoint_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointRouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VPC Endpoint Route Table Association</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the EC2 Route Table to be associated with the VPC Endpoint.</li>
<li><strong>vpc_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_route_table_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_route_table_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointRouteTableAssociation.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointRouteTableAssociation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the EC2 Route Table to be associated with the VPC Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointRouteTableAssociation.vpc_endpoint_id">
<code class="descname">vpc_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointRouteTableAssociation.vpc_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpointRouteTableAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointRouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointRouteTableAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointRouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointService">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpointService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>acceptance_required=None</em>, <em>allowed_principals=None</em>, <em>network_load_balancer_arns=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcEndpointService resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>acceptance_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>allowed_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ARNs of one or more principals allowed to discover the endpoint service.</li>
<li><strong>network_load_balancer_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ARNs of one or more Network Load Balancers for the endpoint service.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.acceptance_required">
<code class="descname">acceptance_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.acceptance_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.allowed_principals">
<code class="descname">allowed_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.allowed_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARNs of one or more principals allowed to discover the endpoint service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zones in which the service is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.base_endpoint_dns_names">
<code class="descname">base_endpoint_dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.base_endpoint_dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS names for the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.manages_vpc_endpoints">
<code class="descname">manages_vpc_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.manages_vpc_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the service manages its VPC endpoints - <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.network_load_balancer_arns">
<code class="descname">network_load_balancer_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.network_load_balancer_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARNs of one or more Network Load Balancers for the endpoint service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.private_dns_name">
<code class="descname">private_dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.private_dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name for the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.service_type">
<code class="descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service type, <code class="docutils literal notranslate"><span class="pre">Gateway</span></code> or <code class="docutils literal notranslate"><span class="pre">Interface</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the VPC endpoint service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointService.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpointService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpointServiceAllowedPrinciple</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>principal_arn=None</em>, <em>vpc_endpoint_service_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcEndpointServiceAllowedPrinciple resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>principal_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the principal to allow permissions.</li>
<li><strong>vpc_endpoint_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC endpoint service to allow permission.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service_allowed_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service_allowed_principal.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.principal_arn">
<code class="descname">principal_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.principal_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the principal to allow permissions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.vpc_endpoint_service_id">
<code class="descname">vpc_endpoint_service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.vpc_endpoint_service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC endpoint service to allow permission.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointServiceAllowedPrinciple.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointSubnetAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcEndpointSubnetAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>subnet_id=None</em>, <em>vpc_endpoint_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointSubnetAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcEndpointSubnetAssociation resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet to be associated with the VPC endpoint.</li>
<li><strong>vpc_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC endpoint with which the subnet will be associated.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_subnet_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_subnet_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointSubnetAssociation.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointSubnetAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet to be associated with the VPC endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcEndpointSubnetAssociation.vpc_endpoint_id">
<code class="descname">vpc_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointSubnetAssociation.vpc_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC endpoint with which the subnet will be associated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcEndpointSubnetAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointSubnetAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcEndpointSubnetAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcEndpointSubnetAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcIpv4CidrBlockAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcIpv4CidrBlockAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cidr_block=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcIpv4CidrBlockAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to associate additional IPv4 CIDR blocks with a VPC.</p>
<p>When a VPC is created, a primary IPv4 CIDR block for the VPC must be specified.
The <code class="docutils literal notranslate"><span class="pre">aws_vpc_ipv4_cidr_block_association</span></code> resource allows further IPv4 CIDR blocks to be added to the VPC.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The additional IPv4 CIDR block to associate with the VPC.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC to make the association with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_ipv4_cidr_block_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_ipv4_cidr_block_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.cidr_block">
<code class="descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The additional IPv4 CIDR block to associate with the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC to make the association with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcIpv4CidrBlockAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcPeeringConnection">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcPeeringConnection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accepter=None</em>, <em>auto_accept=None</em>, <em>peer_owner_id=None</em>, <em>peer_region=None</em>, <em>peer_vpc_id=None</em>, <em>requester=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcPeeringConnection resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>accepter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that accepts
the peering connection (a maximum of one).</li>
<li><strong>auto_accept</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Accept the peering (both VPCs need to be in the same AWS account).</li>
<li><strong>peer_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.</li>
<li><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the accepter VPC of the [VPC Peering Connection]. <code class="docutils literal notranslate"><span class="pre">auto_accept</span></code> must be <code class="docutils literal notranslate"><span class="pre">false</span></code>,
and use the <code class="docutils literal notranslate"><span class="pre">aws_vpc_peering_connection_accepter</span></code> to manage the accepter side.</li>
<li><strong>peer_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC with which you are creating the VPC Peering Connection.</li>
<li><strong>requester</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that requests
the peering connection (a maximum of one).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the requester VPC.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.accept_status">
<code class="descname">accept_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.accept_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the VPC Peering Connection request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.accepter">
<code class="descname">accepter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.accepter" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that accepts
the peering connection (a maximum of one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.auto_accept">
<code class="descname">auto_accept</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.auto_accept" title="Permalink to this definition">¶</a></dt>
<dd><p>Accept the peering (both VPCs need to be in the same AWS account).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.peer_owner_id">
<code class="descname">peer_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.peer_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.peer_region">
<code class="descname">peer_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the accepter VPC of the [VPC Peering Connection]. <code class="docutils literal notranslate"><span class="pre">auto_accept</span></code> must be <code class="docutils literal notranslate"><span class="pre">false</span></code>,
and use the <code class="docutils literal notranslate"><span class="pre">aws_vpc_peering_connection_accepter</span></code> to manage the accepter side.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.peer_vpc_id">
<code class="descname">peer_vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.peer_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC with which you are creating the VPC Peering Connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.requester">
<code class="descname">requester</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.requester" title="Permalink to this definition">¶</a></dt>
<dd><p>A optional configuration block that allows for [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options to be set for the VPC that requests
the peering connection (a maximum of one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the requester VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcPeeringConnection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcPeeringConnection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpcPeeringConnectionAccepter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accepter=None</em>, <em>auto_accept=None</em>, <em>requester=None</em>, <em>tags=None</em>, <em>vpc_peering_connection_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a VPC Peering Connection.</p>
<p>When a cross-account (requester’s AWS account differs from the accepter’s AWS account) or an inter-region
VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter’s account.
The requester can use the <code class="docutils literal notranslate"><span class="pre">aws_vpc_peering_connection</span></code> resource to manage its side of the connection
and the accepter can use the <code class="docutils literal notranslate"><span class="pre">aws_vpc_peering_connection_accepter</span></code> resource to “adopt” its side of the
connection into management.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>accepter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the accepter VPC.</li>
<li><strong>auto_accept</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to accept the peering request. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>requester</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the requester VPC.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Peering Connection ID to manage.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection_accepter.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection_accepter.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.accept_status">
<code class="descname">accept_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.accept_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the VPC Peering Connection request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.accepter">
<code class="descname">accepter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.accepter" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the accepter VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.auto_accept">
<code class="descname">auto_accept</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.auto_accept" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to accept the peering request. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_owner_id">
<code class="descname">peer_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the owner of the requester VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_region">
<code class="descname">peer_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the accepter VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_vpc_id">
<code class="descname">peer_vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.peer_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the requester VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.requester">
<code class="descname">requester</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.requester" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration block that describes [VPC Peering Connection]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide">http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide</a>) options set for the requester VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the accepter VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.vpc_peering_connection_id">
<code class="descname">vpc_peering_connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.vpc_peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Peering Connection ID to manage.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpcPeeringConnectionAccepter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpcPeeringConnectionAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnConnection">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpnConnection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>customer_gateway_id=None</em>, <em>static_routes_only=None</em>, <em>tags=None</em>, <em>transit_gateway_id=None</em>, <em>tunnel1_inside_cidr=None</em>, <em>tunnel1_preshared_key=None</em>, <em>tunnel2_inside_cidr=None</em>, <em>tunnel2_preshared_key=None</em>, <em>type=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including <code class="docutils literal notranslate"><span class="pre">tunnel1_preshared_key</span></code> and <code class="docutils literal notranslate"><span class="pre">tunnel2_preshared_key</span></code> will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p><strong>Note:</strong> The CIDR blocks in the arguments <code class="docutils literal notranslate"><span class="pre">tunnel1_inside_cidr</span></code> and <code class="docutils literal notranslate"><span class="pre">tunnel2_inside_cidr</span></code> must have a prefix of /30 and be a part of a specific range.
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html">Read more about this in the AWS documentation</a>.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>customer_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the customer gateway.</li>
<li><strong>static_routes_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don’t support BGP.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Tags to apply to the connection.</li>
<li><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EC2 Transit Gateway.</li>
<li><strong>tunnel1_inside_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block of the inside IP addresses for the first VPN tunnel.</li>
<li><strong>tunnel1_preshared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preshared key of the first VPN tunnel.</li>
<li><strong>tunnel2_inside_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block of the second IP addresses for the first VPN tunnel.</li>
<li><strong>tunnel2_preshared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preshared key of the second VPN tunnel.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of VPN connection. The only type AWS supports at this time is “ipsec.1”.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Private Gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_connection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.customer_gateway_configuration">
<code class="descname">customer_gateway_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.customer_gateway_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration information for the VPN connection’s customer gateway (in the native XML format).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.customer_gateway_id">
<code class="descname">customer_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.customer_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the customer gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.static_routes_only">
<code class="descname">static_routes_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.static_routes_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don’t support BGP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to apply to the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.transit_gateway_attachment_id">
<code class="descname">transit_gateway_attachment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When associated with an EC2 Transit Gateway (<code class="docutils literal notranslate"><span class="pre">transit_gateway_id</span></code> argument), the attachment ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_address">
<code class="descname">tunnel1_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address of the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_bgp_asn">
<code class="descname">tunnel1_bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The bgp asn number of the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_bgp_holdtime">
<code class="descname">tunnel1_bgp_holdtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_bgp_holdtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The bgp holdtime of the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_cgw_inside_address">
<code class="descname">tunnel1_cgw_inside_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_cgw_inside_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_inside_cidr">
<code class="descname">tunnel1_inside_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_inside_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block of the inside IP addresses for the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_preshared_key">
<code class="descname">tunnel1_preshared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_preshared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The preshared key of the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel1_vgw_inside_address">
<code class="descname">tunnel1_vgw_inside_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel1_vgw_inside_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_address">
<code class="descname">tunnel2_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address of the second VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_bgp_asn">
<code class="descname">tunnel2_bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The bgp asn number of the second VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_bgp_holdtime">
<code class="descname">tunnel2_bgp_holdtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_bgp_holdtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The bgp holdtime of the second VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_cgw_inside_address">
<code class="descname">tunnel2_cgw_inside_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_cgw_inside_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_inside_cidr">
<code class="descname">tunnel2_inside_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_inside_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block of the second IP addresses for the first VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_preshared_key">
<code class="descname">tunnel2_preshared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_preshared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The preshared key of the second VPN tunnel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.tunnel2_vgw_inside_address">
<code class="descname">tunnel2_vgw_inside_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.tunnel2_vgw_inside_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of VPN connection. The only type AWS supports at this time is “ipsec.1”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnection.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Private Gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpnConnection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnConnection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnConnectionRoute">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpnConnectionRoute</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_cidr_block=None</em>, <em>vpn_connection_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnectionRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a static route between a VPN connection and a customer gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destination_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block associated with the local subnet of the customer network.</li>
<li><strong>vpn_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_connection_route.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_connection_route.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnectionRoute.destination_cidr_block">
<code class="descname">destination_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnectionRoute.destination_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block associated with the local subnet of the customer network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnConnectionRoute.vpn_connection_id">
<code class="descname">vpn_connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnConnectionRoute.vpn_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPN connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpnConnectionRoute.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnectionRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnConnectionRoute.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnConnectionRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpnGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>amazon_side_asn=None</em>, <em>availability_zone=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a VPC VPN Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don’t specify an ASN, the virtual private gateway is created with the default ASN.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone for the virtual private gateway.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID to create in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGateway.amazon_side_asn">
<code class="descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don’t specify an ASN, the virtual private gateway is created with the default ASN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGateway.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone for the virtual private gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGateway.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID to create in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpnGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGatewayAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpnGatewayAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>vpc_id=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Virtual Private Gateway attachment resource, allowing for an existing
hardware VPN gateway to be attached and/or detached from a VPC.</p>
<blockquote>
<div><strong>Note:</strong> The <code class="docutils literal notranslate"><span class="pre">aws_vpn_gateway</span></code>
resource can also automatically attach the Virtual Private Gateway it creates
to an existing VPC by setting the <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> attribute accordingly.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Private Gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGatewayAttachment.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayAttachment.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGatewayAttachment.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayAttachment.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Private Gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpnGatewayAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGatewayAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGatewayRoutePropagation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2.</code><code class="descname">VpnGatewayRoutePropagation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>route_table_id=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayRoutePropagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests automatic route propagation between a VPN gateway and a route table.</p>
<blockquote>
<div><strong>Note:</strong> This resource should not be used with a route table that has
the <code class="docutils literal notranslate"><span class="pre">propagating_vgws</span></code> argument set. If that argument is set, any route
propagation not explicitly listed in its value will be removed.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the <code class="docutils literal notranslate"><span class="pre">aws_route_table</span></code> to propagate routes into.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the <code class="docutils literal notranslate"><span class="pre">aws_vpn_gateway</span></code> to propagate routes from.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway_route_propagation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_gateway_route_propagation.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGatewayRoutePropagation.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayRoutePropagation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the <code class="docutils literal notranslate"><span class="pre">aws_route_table</span></code> to propagate routes into.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2.VpnGatewayRoutePropagation.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayRoutePropagation.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the <code class="docutils literal notranslate"><span class="pre">aws_vpn_gateway</span></code> to propagate routes from.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2.VpnGatewayRoutePropagation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayRoutePropagation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.VpnGatewayRoutePropagation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.VpnGatewayRoutePropagation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2.get_customer_gateway">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_customer_gateway</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_customer_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AWS Customer Gateway.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/customer_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/customer_gateway.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_instance">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_instance</code><span class="sig-paren">(</span><em>filters=None</em>, <em>get_password_data=None</em>, <em>get_user_data=None</em>, <em>instance_id=None</em>, <em>instance_tags=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an Amazon EC2 Instance for use in other
resources.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/instance.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_instances">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_instances</code><span class="sig-paren">(</span><em>filters=None</em>, <em>instance_state_names=None</em>, <em>instance_tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/instances.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/instances.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_internet_gateway">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_internet_gateway</code><span class="sig-paren">(</span><em>filters=None</em>, <em>internet_gateway_id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_internet_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_internet_gateway</span></code> provides details about a specific Internet Gateway.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/internet_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/internet_gateway.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_launch_configuration">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_launch_configuration</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_launch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Launch Configuration.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_configuration.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_launch_template">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_launch_template</code><span class="sig-paren">(</span><em>name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_launch_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Launch Template.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_template.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_nat_gateway">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_nat_gateway</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>state=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Nat Gateway.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/nat_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/nat_gateway.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_network_interface">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_network_interface</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_network_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Network Interface.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/network_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/network_interface.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_route">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_route</code><span class="sig-paren">(</span><em>destination_cidr_block=None</em>, <em>destination_ipv6_cidr_block=None</em>, <em>egress_only_gateway_id=None</em>, <em>gateway_id=None</em>, <em>instance_id=None</em>, <em>nat_gateway_id=None</em>, <em>network_interface_id=None</em>, <em>route_table_id=None</em>, <em>transit_gateway_id=None</em>, <em>vpc_peering_connection_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_route" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_route</span></code> provides details about a specific Route.</p>
<p>This resource can prove useful when finding the resource
associated with a CIDR. For example, finding the peering
connection associated with a CIDR value.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_route_table">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_route_table</code><span class="sig-paren">(</span><em>filters=None</em>, <em>route_table_id=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_route_table</span></code> provides details about a specific Route Table.</p>
<p>This resource can prove useful when a module accepts a Subnet id as
an input variable and needs to, for example, add a route in
the Route Table.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_table.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_table.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_route_tables">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_route_tables</code><span class="sig-paren">(</span><em>filters=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_route_tables" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource can be useful for getting back a list of route table ids to be referenced elsewhere.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_tables.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_tables.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_security_group">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_security_group</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> provides details about a specific Security Group.</p>
<p>This resource can prove useful when a module accepts a Security Group id as
an input variable and needs to, for example, determine the id of the
VPC that the security group belongs to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_security_groups">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_security_groups</code><span class="sig-paren">(</span><em>filters=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_groups.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_groups.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_subnet">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_subnet</code><span class="sig-paren">(</span><em>availability_zone=None</em>, <em>availability_zone_id=None</em>, <em>cidr_block=None</em>, <em>default_for_az=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>ipv6_cidr_block=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_subnet</span></code> provides details about a specific VPC subnet.</p>
<p>This resource can prove useful when a module accepts a subnet id as
an input variable and needs to, for example, determine the id of the
VPC that the subnet belongs to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/subnet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/subnet.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_subnet_ids">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_subnet_ids</code><span class="sig-paren">(</span><em>filters=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_subnet_ids</span></code> provides a list of ids for a vpc_id</p>
<p>This resource can be useful for getting back a list of subnet ids for a vpc.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/subnet_ids.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/subnet_ids.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpc">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpc</code><span class="sig-paren">(</span><em>cidr_block=None</em>, <em>default=None</em>, <em>dhcp_options_id=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpc" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_vpc</span></code> provides details about a specific VPC.</p>
<p>This resource can prove useful when a module accepts a vpc id as
an input variable and needs to, for example, determine the CIDR block of that
VPC.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpc_dhcp_options">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpc_dhcp_options</code><span class="sig-paren">(</span><em>dhcp_options_id=None</em>, <em>filters=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpc_dhcp_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an EC2 DHCP Options configuration.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_dhcp_options.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_dhcp_options.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpc_endpoint">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpc_endpoint</code><span class="sig-paren">(</span><em>id=None</em>, <em>service_name=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpc_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Endpoint data source provides details about
a specific VPC endpoint.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_endpoint.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpc_endpoint_service">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpc_endpoint_service</code><span class="sig-paren">(</span><em>service=None</em>, <em>service_name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpc_endpoint_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Endpoint Service data source details about a specific service that
can be specified when creating a VPC endpoint within the region configured in the provider.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_endpoint_service.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_endpoint_service.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpc_peering_connection">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpc_peering_connection</code><span class="sig-paren">(</span><em>cidr_block=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>owner_id=None</em>, <em>peer_cidr_block=None</em>, <em>peer_owner_id=None</em>, <em>peer_region=None</em>, <em>peer_vpc_id=None</em>, <em>region=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpc_peering_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Peering Connection data source provides details about
a specific VPC peering connection.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_peering_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpc_peering_connection.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpcs">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpcs</code><span class="sig-paren">(</span><em>filters=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpcs" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource can be useful for getting back a list of VPC Ids for a region.</p>
<p>The following example retrieves a list of VPC Ids with a custom tag of <code class="docutils literal notranslate"><span class="pre">service</span></code> set to a value of “production”.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpcs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpcs.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2.get_vpn_gateway">
<code class="descclassname">pulumi_aws.ec2.</code><code class="descname">get_vpn_gateway</code><span class="sig-paren">(</span><em>amazon_side_asn=None</em>, <em>attached_vpc_id=None</em>, <em>availability_zone=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2.get_vpn_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPN Gateway data source provides details about
a specific VPN gateway.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/vpn_gateway.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
