---
title: Module fsx
title_tag: Module fsx | Package pulumi_aws | Python SDK
linktitle: fsx
notitle: true
---

<div class="section" id="fsx">
<h1>fsx<a class="headerlink" href="#fsx" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.fsx"></span><dl class="class">
<dt id="pulumi_aws.fsx.LustreFileSystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.fsx.</code><code class="sig-name descname">LustreFileSystem</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">export_path=None</em>, <em class="sig-param">import_path=None</em>, <em class="sig-param">imported_file_chunk_size=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">storage_capacity=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">weekly_maintenance_start_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a FSx Lustre File System. See the <a class="reference external" href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html">FSx Lustre Guide</a> for more information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/fsx_lustre_file_system.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/fsx_lustre_file_system.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>export_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument and the path must use the same Amazon S3 bucket as specified in <code class="docutils literal notranslate"><span class="pre">import_path</span></code>. Set equal to <code class="docutils literal notranslate"><span class="pre">import_path</span></code> to overwrite files on export. Defaults to <code class="docutils literal notranslate"><span class="pre">s3://{IMPORT</span> <span class="pre">BUCKET}/FSxLustre{CREATION</span> <span class="pre">TIMESTAMP}</span></code>.</p></li>
<li><p><strong>import_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 URI (with optional prefix) that you’re using as the data repository for your FSx for Lustre file system. For example, <code class="docutils literal notranslate"><span class="pre">s3://example-bucket/optional-prefix/</span></code>.</p></li>
<li><p><strong>imported_file_chunk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument. Defaults to <code class="docutils literal notranslate"><span class="pre">1024</span></code>. Minimum of <code class="docutils literal notranslate"><span class="pre">1</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">512000</span></code>.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p></li>
<li><p><strong>storage_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The storage capacity (GiB) of the file system. Minimum of <code class="docutils literal notranslate"><span class="pre">1200</span></code>. Storage capacity is provisioned in increments of 3,600 GiB.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>weekly_maintenance_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS name for the file system, e.g. <code class="docutils literal notranslate"><span class="pre">fs-12345678.fsx.us-west-2.amazonaws.com</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.export_path">
<code class="sig-name descname">export_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.export_path" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument and the path must use the same Amazon S3 bucket as specified in <code class="docutils literal notranslate"><span class="pre">import_path</span></code>. Set equal to <code class="docutils literal notranslate"><span class="pre">import_path</span></code> to overwrite files on export. Defaults to <code class="docutils literal notranslate"><span class="pre">s3://{IMPORT</span> <span class="pre">BUCKET}/FSxLustre{CREATION</span> <span class="pre">TIMESTAMP}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.import_path">
<code class="sig-name descname">import_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.import_path" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 URI (with optional prefix) that you’re using as the data repository for your FSx for Lustre file system. For example, <code class="docutils literal notranslate"><span class="pre">s3://example-bucket/optional-prefix/</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.imported_file_chunk_size">
<code class="sig-name descname">imported_file_chunk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.imported_file_chunk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument. Defaults to <code class="docutils literal notranslate"><span class="pre">1024</span></code>. Minimum of <code class="docutils literal notranslate"><span class="pre">1</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">512000</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.network_interface_ids">
<code class="sig-name descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of Elastic Network Interface identifiers from which the file system is accessible.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account identifier that created the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.storage_capacity">
<code class="sig-name descname">storage_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.storage_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage capacity (GiB) of the file system. Minimum of <code class="docutils literal notranslate"><span class="pre">1200</span></code>. Storage capacity is provisioned in increments of 3,600 GiB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the Virtual Private Cloud for the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.LustreFileSystem.weekly_maintenance_start_time">
<code class="sig-name descname">weekly_maintenance_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.weekly_maintenance_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.fsx.LustreFileSystem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">export_path=None</em>, <em class="sig-param">import_path=None</em>, <em class="sig-param">imported_file_chunk_size=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">storage_capacity=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">weekly_maintenance_start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LustreFileSystem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the file system.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS name for the file system, e.g. <code class="docutils literal notranslate"><span class="pre">fs-12345678.fsx.us-west-2.amazonaws.com</span></code></p></li>
<li><p><strong>export_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument and the path must use the same Amazon S3 bucket as specified in <code class="docutils literal notranslate"><span class="pre">import_path</span></code>. Set equal to <code class="docutils literal notranslate"><span class="pre">import_path</span></code> to overwrite files on export. Defaults to <code class="docutils literal notranslate"><span class="pre">s3://{IMPORT</span> <span class="pre">BUCKET}/FSxLustre{CREATION</span> <span class="pre">TIMESTAMP}</span></code>.</p></li>
<li><p><strong>import_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 URI (with optional prefix) that you’re using as the data repository for your FSx for Lustre file system. For example, <code class="docutils literal notranslate"><span class="pre">s3://example-bucket/optional-prefix/</span></code>.</p></li>
<li><p><strong>imported_file_chunk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with <code class="docutils literal notranslate"><span class="pre">import_path</span></code> argument. Defaults to <code class="docutils literal notranslate"><span class="pre">1024</span></code>. Minimum of <code class="docutils literal notranslate"><span class="pre">1</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">512000</span></code>.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of Elastic Network Interface identifiers from which the file system is accessible.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account identifier that created the file system.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p></li>
<li><p><strong>storage_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The storage capacity (GiB) of the file system. Minimum of <code class="docutils literal notranslate"><span class="pre">1200</span></code>. Storage capacity is provisioned in increments of 3,600 GiB.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the Virtual Private Cloud for the file system.</p></li>
<li><p><strong>weekly_maintenance_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.fsx.LustreFileSystem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.fsx.LustreFileSystem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.LustreFileSystem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.fsx.WindowsFileSystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.fsx.</code><code class="sig-name descname">WindowsFileSystem</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_directory_id=None</em>, <em class="sig-param">automatic_backup_retention_days=None</em>, <em class="sig-param">copy_tags_to_backups=None</em>, <em class="sig-param">daily_automatic_backup_start_time=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">self_managed_active_directory=None</em>, <em class="sig-param">skip_final_backup=None</em>, <em class="sig-param">storage_capacity=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">throughput_capacity=None</em>, <em class="sig-param">weekly_maintenance_start_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a FSx Windows File System. See the <a class="reference external" href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html">FSx Windows Guide</a> for more information.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Either the <code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code> argument or <code class="docutils literal notranslate"><span class="pre">self_managed_active_directory</span></code> configuration block must be specified.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/fsx_windows_file_system.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/fsx_windows_file_system.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for an existing Microsoft Active Directory instance that the file system should join when it’s created. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">self_managed_active_directory</span></code>.</p></li>
<li><p><strong>automatic_backup_retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to retain automatic backups. Minimum of <code class="docutils literal notranslate"><span class="pre">0</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">35</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">7</span></code>. Set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to disable.</p></li>
<li><p><strong>copy_tags_to_backups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>daily_automatic_backup_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred time (in <code class="docutils literal notranslate"><span class="pre">HH:MM</span></code> format) to take daily automatic backups, in the UTC time zone.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p></li>
<li><p><strong>self_managed_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code>. Detailed below.</p></li>
<li><p><strong>skip_final_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>storage_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>throughput_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of <code class="docutils literal notranslate"><span class="pre">8</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p></li>
<li><p><strong>weekly_maintenance_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>self_managed_active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in <a class="reference external" href="https://tools.ietf.org/html/rfc1918">RFC 1918</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified domain name of the self-managed AD directory. For example, <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystemAdministratorsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to <code class="docutils literal notranslate"><span class="pre">Domain</span> <span class="pre">Admins</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnitDistinguishedName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, <code class="docutils literal notranslate"><span class="pre">OU=FSx,DC=yourdomain,DC=corp,DC=com</span></code>. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see <a class="reference external" href="https://tools.ietf.org/html/rfc2253">RFC 2253</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.active_directory_id">
<code class="sig-name descname">active_directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.active_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for an existing Microsoft Active Directory instance that the file system should join when it’s created. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">self_managed_active_directory</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.automatic_backup_retention_days">
<code class="sig-name descname">automatic_backup_retention_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.automatic_backup_retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days to retain automatic backups. Minimum of <code class="docutils literal notranslate"><span class="pre">0</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">35</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">7</span></code>. Set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to disable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.copy_tags_to_backups">
<code class="sig-name descname">copy_tags_to_backups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.copy_tags_to_backups" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.daily_automatic_backup_start_time">
<code class="sig-name descname">daily_automatic_backup_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.daily_automatic_backup_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The preferred time (in <code class="docutils literal notranslate"><span class="pre">HH:MM</span></code> format) to take daily automatic backups, in the UTC time zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS name for the file system, e.g. <code class="docutils literal notranslate"><span class="pre">fs-12345678.corp.example.com</span></code> (domain name matching the Active Directory domain name)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.network_interface_ids">
<code class="sig-name descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of Elastic Network Interface identifiers from which the file system is accessible.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account identifier that created the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.self_managed_active_directory">
<code class="sig-name descname">self_managed_active_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.self_managed_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code>. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in <a class="reference external" href="https://tools.ietf.org/html/rfc1918">RFC 1918</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified domain name of the self-managed AD directory. For example, <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystemAdministratorsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to <code class="docutils literal notranslate"><span class="pre">Domain</span> <span class="pre">Admins</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnitDistinguishedName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, <code class="docutils literal notranslate"><span class="pre">OU=FSx,DC=yourdomain,DC=corp,DC=com</span></code>. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see <a class="reference external" href="https://tools.ietf.org/html/rfc2253">RFC 2253</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.skip_final_backup">
<code class="sig-name descname">skip_final_backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.skip_final_backup" title="Permalink to this definition">¶</a></dt>
<dd><p>When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.storage_capacity">
<code class="sig-name descname">storage_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.storage_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.throughput_capacity">
<code class="sig-name descname">throughput_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.throughput_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of <code class="docutils literal notranslate"><span class="pre">8</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the Virtual Private Cloud for the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.fsx.WindowsFileSystem.weekly_maintenance_start_time">
<code class="sig-name descname">weekly_maintenance_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.weekly_maintenance_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.fsx.WindowsFileSystem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_directory_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">automatic_backup_retention_days=None</em>, <em class="sig-param">copy_tags_to_backups=None</em>, <em class="sig-param">daily_automatic_backup_start_time=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">self_managed_active_directory=None</em>, <em class="sig-param">skip_final_backup=None</em>, <em class="sig-param">storage_capacity=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">throughput_capacity=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">weekly_maintenance_start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WindowsFileSystem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for an existing Microsoft Active Directory instance that the file system should join when it’s created. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">self_managed_active_directory</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the file system.</p></li>
<li><p><strong>automatic_backup_retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to retain automatic backups. Minimum of <code class="docutils literal notranslate"><span class="pre">0</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">35</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">7</span></code>. Set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to disable.</p></li>
<li><p><strong>copy_tags_to_backups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>daily_automatic_backup_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred time (in <code class="docutils literal notranslate"><span class="pre">HH:MM</span></code> format) to take daily automatic backups, in the UTC time zone.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS name for the file system, e.g. <code class="docutils literal notranslate"><span class="pre">fs-12345678.corp.example.com</span></code> (domain name matching the Active Directory domain name)</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of Elastic Network Interface identifiers from which the file system is accessible.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account identifier that created the file system.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.</p></li>
<li><p><strong>self_managed_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with <code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code>. Detailed below.</p></li>
<li><p><strong>skip_final_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>storage_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet’s Availability Zone.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the file system.</p></li>
<li><p><strong>throughput_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of <code class="docutils literal notranslate"><span class="pre">8</span></code> and maximum of <code class="docutils literal notranslate"><span class="pre">2048</span></code>.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the Virtual Private Cloud for the file system.</p></li>
<li><p><strong>weekly_maintenance_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The preferred start time (in <code class="docutils literal notranslate"><span class="pre">d:HH:MM</span></code> format) to perform weekly maintenance, in the UTC time zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>self_managed_active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in <a class="reference external" href="https://tools.ietf.org/html/rfc1918">RFC 1918</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified domain name of the self-managed AD directory. For example, <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystemAdministratorsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to <code class="docutils literal notranslate"><span class="pre">Domain</span> <span class="pre">Admins</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnitDistinguishedName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, <code class="docutils literal notranslate"><span class="pre">OU=FSx,DC=yourdomain,DC=corp,DC=com</span></code>. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see <a class="reference external" href="https://tools.ietf.org/html/rfc2253">RFC 2253</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.fsx.WindowsFileSystem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.fsx.WindowsFileSystem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.fsx.WindowsFileSystem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
