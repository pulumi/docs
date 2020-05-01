---
title: Module efs
title_tag: Module efs | Package pulumi_aws | Python SDK
linktitle: efs
notitle: true
---

<div class="section" id="efs">
<h1>efs<a class="headerlink" href="#efs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.efs"></span><dl class="py class">
<dt id="pulumi_aws.efs.AwaitableGetFileSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AwaitableGetFileSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AwaitableGetFileSystemResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.AwaitableGetMountTargetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AwaitableGetMountTargetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AwaitableGetMountTargetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.FileSystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">FileSystem</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic File System (EFS) resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>creation_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(<a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/">http://docs.aws.amazon.com/efs/latest/ug/</a>) user guide for more information.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.</p></li>
<li><p><strong>lifecycle_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A file system <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html">lifecycle policy</a> object (documented below).</p></li>
<li><p><strong>performance_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file system performance mode. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;maxIO&quot;</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code>).</p></li>
<li><p><strong>provisioned_throughput_in_mibps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with <code class="docutils literal notranslate"><span class="pre">throughput_mode</span></code> set to <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>throughput_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Throughput mode for the file system. Defaults to <code class="docutils literal notranslate"><span class="pre">bursting</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">bursting</span></code>, <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>. When using <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>, also set <code class="docutils literal notranslate"><span class="pre">provisioned_throughput_in_mibps</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifecycle_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">transitionToIa</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates how long it takes to transition files to the IA storage class. Valid values: <code class="docutils literal notranslate"><span class="pre">AFTER_7_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_14_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_30_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_60_DAYS</span></code>, or <code class="docutils literal notranslate"><span class="pre">AFTER_90_DAYS</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.creation_token">
<code class="sig-name descname">creation_token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.creation_token" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(<a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/">http://docs.aws.amazon.com/efs/latest/ug/</a>) user guide for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.dns_name">
<code class="sig-name descname">dns_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name for the filesystem per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.encrypted">
<code class="sig-name descname">encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the disk will be encrypted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.lifecycle_policy">
<code class="sig-name descname">lifecycle_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.lifecycle_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A file system <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html">lifecycle policy</a> object (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">transitionToIa</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates how long it takes to transition files to the IA storage class. Valid values: <code class="docutils literal notranslate"><span class="pre">AFTER_7_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_14_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_30_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_60_DAYS</span></code>, or <code class="docutils literal notranslate"><span class="pre">AFTER_90_DAYS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.performance_mode">
<code class="sig-name descname">performance_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.performance_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The file system performance mode. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;maxIO&quot;</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.provisioned_throughput_in_mibps">
<code class="sig-name descname">provisioned_throughput_in_mibps</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.provisioned_throughput_in_mibps" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with <code class="docutils literal notranslate"><span class="pre">throughput_mode</span></code> set to <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystem.throughput_mode">
<code class="sig-name descname">throughput_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystem.throughput_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Throughput mode for the file system. Defaults to <code class="docutils literal notranslate"><span class="pre">bursting</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">bursting</span></code>, <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>. When using <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>, also set <code class="docutils literal notranslate"><span class="pre">provisioned_throughput_in_mibps</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.FileSystem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FileSystem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the file system.</p></li>
<li><p><strong>creation_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(<a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/">http://docs.aws.amazon.com/efs/latest/ug/</a>) user guide for more information.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The DNS name for the filesystem per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.</p></li>
<li><p><strong>lifecycle_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A file system <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html">lifecycle policy</a> object (documented below).</p>
</p></li>
<li><p><strong>performance_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file system performance mode. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;maxIO&quot;</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">&quot;generalPurpose&quot;</span></code>).</p></li>
<li><p><strong>provisioned_throughput_in_mibps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with <code class="docutils literal notranslate"><span class="pre">throughput_mode</span></code> set to <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>throughput_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Throughput mode for the file system. Defaults to <code class="docutils literal notranslate"><span class="pre">bursting</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">bursting</span></code>, <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>. When using <code class="docutils literal notranslate"><span class="pre">provisioned</span></code>, also set <code class="docutils literal notranslate"><span class="pre">provisioned_throughput_in_mibps</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifecycle_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">transitionToIa</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates how long it takes to transition files to the IA storage class. Valid values: <code class="docutils literal notranslate"><span class="pre">AFTER_7_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_14_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_30_DAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">AFTER_60_DAYS</span></code>, or <code class="docutils literal notranslate"><span class="pre">AFTER_90_DAYS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.FileSystem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.FileSystem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.GetFileSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">GetFileSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFileSystem.</p>
<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name for the filesystem per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether EFS is encrypted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.lifecycle_policy">
<code class="sig-name descname">lifecycle_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.lifecycle_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A file system <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html">lifecycle policy</a> object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.performance_mode">
<code class="sig-name descname">performance_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.performance_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The file system performance mode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.provisioned_throughput_in_mibps">
<code class="sig-name descname">provisioned_throughput_in_mibps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.provisioned_throughput_in_mibps" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput, measured in MiB/s, that you want to provision for the file system.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> -A mapping of tags to assign to the file system.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.throughput_mode">
<code class="sig-name descname">throughput_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.throughput_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Throughput mode for the file system.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.GetMountTargetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">GetMountTargetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMountTarget.</p>
<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name for the given subnet/AZ per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.file_system_arn">
<code class="sig-name descname">file_system_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system for which the mount target is intended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the file system for which the mount target is intended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Address at which the file system may be mounted via the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface that Amazon EFS created when it created the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.security_groups">
<code class="sig-name descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of VPC security group IDs attached to the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetMountTargetResult.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetMountTargetResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the mount target’s subnet.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.MountTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">MountTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.MountTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic File System (EFS) mount target.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the file system for which the mount target is intended.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address (within the address range of the specified subnet) at
which the file system may be mounted via the mount target.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of up to 5 VPC security group IDs (that must
be for the same VPC as subnet specified) in effect for the mount target.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet to add the mount target in.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.dns_name">
<code class="sig-name descname">dns_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name for the given subnet/AZ per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.file_system_arn">
<code class="sig-name descname">file_system_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the file system for which the mount target is intended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address (within the address range of the specified subnet) at
which the file system may be mounted via the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface that Amazon EFS created when it created the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of up to 5 VPC security group IDs (that must
be for the same VPC as subnet specified) in effect for the mount target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.MountTarget.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.MountTarget.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet to add the mount target in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.MountTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.MountTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MountTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The DNS name for the given subnet/AZ per <a class="reference external" href="http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html">documented convention</a>.</p>
</p></li>
<li><p><strong>file_system_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the file system.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the file system for which the mount target is intended.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address (within the address range of the specified subnet) at
which the file system may be mounted via the mount target.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network interface that Amazon EFS created when it created the mount target.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of up to 5 VPC security group IDs (that must
be for the same VPC as subnet specified) in effect for the mount target.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet to add the mount target in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.MountTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.MountTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.MountTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.MountTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.get_file_system">
<code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">get_file_system</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.get_file_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about an Elastic File System (EFS).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>creation_token</strong> (<em>str</em>) – Restricts the list to the file system with this creation token.</p></li>
<li><p><strong>file_system_id</strong> (<em>str</em>) – The ID that identifies the file system (e.g. fs-ccfc0d65).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.efs.get_mount_target">
<code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">get_mount_target</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">mount_target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.get_mount_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about an Elastic File System Mount Target (EFS).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mount_target_id</strong> (<em>str</em>) – ID of the mount target that you want to have described</p>
</dd>
</dl>
</dd></dl>

</div>
