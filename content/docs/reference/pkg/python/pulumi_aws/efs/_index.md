---
title: Module efs
title_tag: Module efs | Package pulumi_aws | Python SDK
linktitle: efs
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "aws" >}}

<div class="section" id="efs">
<h1>efs<a class="headerlink" href="#efs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.efs"></span><dl class="py class">
<dt id="pulumi_aws.efs.AccessPoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AccessPoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">posix_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AccessPoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic File System (EFS) access point.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">AccessPoint</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span> <span class="n">file_system_id</span><span class="o">=</span><span class="n">aws_efs_file_system</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the file system for which the access point is intended.</p></li>
<li><p><strong>posix_user</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The operating system user and group applied to all file system requests made using the access point. See Posix User below.</p></li>
<li><p><strong>root_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>posix_user</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The POSIX group ID used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryGids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Secondary POSIX group IDs used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - he POSIX user ID used for all file system operations using this access point.</p></li>
</ul>
<p>The <strong>root_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creationInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the POSIX IDs and permissions to apply to the access point’s Root Directory. See Creation Info below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the POSIX group ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the POSIX user ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file’s mode bits.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide <code class="docutils literal notranslate"><span class="pre">creation_info</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the access point.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.file_system_arn">
<code class="sig-name descname">file_system_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the file system for which the access point is intended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.posix_user">
<code class="sig-name descname">posix_user</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.posix_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system user and group applied to all file system requests made using the access point. See Posix User below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The POSIX group ID used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryGids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Secondary POSIX group IDs used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - he POSIX user ID used for all file system operations using this access point.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.root_directory">
<code class="sig-name descname">root_directory</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.root_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creationInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the POSIX IDs and permissions to apply to the access point’s Root Directory. See Creation Info below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerGid</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the POSIX group ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerUid</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the POSIX user ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file’s mode bits.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide <code class="docutils literal notranslate"><span class="pre">creation_info</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.AccessPoint.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.AccessPoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">posix_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the access point.</p></li>
<li><p><strong>file_system_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name of the file system.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the file system for which the access point is intended.</p></li>
<li><p><strong>posix_user</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The operating system user and group applied to all file system requests made using the access point. See Posix User below.</p></li>
<li><p><strong>root_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the directory on the Amazon EFS file system that the access point provides access to. See Root Directory below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>posix_user</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The POSIX group ID used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryGids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Secondary POSIX group IDs used for all file system operations using this access point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - he POSIX user ID used for all file system operations using this access point.</p></li>
</ul>
<p>The <strong>root_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creationInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the POSIX IDs and permissions to apply to the access point’s Root Directory. See Creation Info below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the POSIX group ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ownerUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the POSIX user ID to apply to the <code class="docutils literal notranslate"><span class="pre">root_directory</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file’s mode bits.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide <code class="docutils literal notranslate"><span class="pre">creation_info</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.AccessPoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.AccessPoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AccessPoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.AwaitableGetAccessPointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AwaitableGetAccessPointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_point_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">posix_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_directories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AwaitableGetAccessPointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.AwaitableGetFileSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AwaitableGetFileSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_in_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AwaitableGetFileSystemResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.AwaitableGetMountTargetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">AwaitableGetMountTargetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.AwaitableGetMountTargetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.FileSystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">FileSystem</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic File System (EFS) File System resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">FileSystem</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;MyProduct&quot;</span><span class="p">,</span>
<span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo_with_lifecyle_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">FileSystem</span><span class="p">(</span><span class="s2">&quot;fooWithLifecylePolicy&quot;</span><span class="p">,</span> <span class="n">lifecycle_policy</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;transitionToIa&quot;</span><span class="p">:</span> <span class="s2">&quot;AFTER_30_DAYS&quot;</span><span class="p">,</span>
<span class="p">})</span>
</pre></div>
</div>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the file system.</p></li>
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
<dd><p>A map of tags to assign to the file system.</p>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the file system.</p></li>
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
<dt id="pulumi_aws.efs.FileSystemPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">FileSystemPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic File System (EFS) File System Policy resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">fs</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">FileSystem</span><span class="p">(</span><span class="s2">&quot;fs&quot;</span><span class="p">)</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">FileSystemPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">file_system_id</span><span class="o">=</span><span class="n">fs</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Id&quot;: &quot;ExamplePolicy01&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [</span>
<span class="s2">        </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">            &quot;Sid&quot;: &quot;ExampleSatement01&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;AWS&quot;: &quot;*&quot;</span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">            &quot;Resource&quot;: &quot;</span><span class="si">{</span><span class="n">aws_efs_file_system</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;,</span>
<span class="s2">            &quot;Action&quot;: [</span>
<span class="s2">                &quot;elasticfilesystem:ClientMount&quot;,</span>
<span class="s2">                &quot;elasticfilesystem:ClientWrite&quot;</span>
<span class="s2">            ],</span>
<span class="s2">            &quot;Condition&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;Bool&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;aws:SecureTransport&quot;: &quot;true&quot;</span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    ]</span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EFS file system.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON formatted file system policy for the EFS file system. see <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies">Docs</a> for more info.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystemPolicy.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the EFS file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.FileSystemPolicy.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON formatted file system policy for the EFS file system. see <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies">Docs</a> for more info.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.FileSystemPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FileSystemPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EFS file system.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The JSON formatted file system policy for the EFS file system. see <a class="reference external" href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies">Docs</a> for more info.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.efs.FileSystemPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.FileSystemPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.FileSystemPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.efs.GetAccessPointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">GetAccessPointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_point_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">posix_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_directories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessPoint.</p>
<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.file_system_arn">
<code class="sig-name descname">file_system_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name of the file system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the file system for which the access point is intended.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.posix_users">
<code class="sig-name descname">posix_users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.posix_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Single element list containing operating system user and group applied to all file system requests made using the access point.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetAccessPointResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetAccessPointResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.efs.GetFileSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">GetFileSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned_throughput_in_mibps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_in_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput_mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> -A map of tags to assign to the file system.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.efs.GetFileSystemResult.size_in_bytes">
<code class="sig-name descname">size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.efs.GetFileSystemResult.size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The current byte count used by the file system.</p>
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
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Vpc</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/16&quot;</span><span class="p">)</span>
<span class="n">alpha_subnet</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;alphaSubnet&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="s2">&quot;us-west-2a&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">alpha_mount_target</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">MountTarget</span><span class="p">(</span><span class="s2">&quot;alphaMountTarget&quot;</span><span class="p">,</span>
    <span class="n">file_system_id</span><span class="o">=</span><span class="n">aws_efs_file_system</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">subnet_id</span><span class="o">=</span><span class="n">alpha_subnet</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
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
<dt id="pulumi_aws.efs.get_access_point">
<code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">get_access_point</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_point_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.get_access_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about an Elastic File System (EFS) Access Point.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">get_access_point</span><span class="p">(</span><span class="n">access_point_id</span><span class="o">=</span><span class="s2">&quot;fsap-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>access_point_id</strong> (<em>str</em>) – The ID that identifies the file system.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.efs.get_file_system">
<code class="sig-prename descclassname">pulumi_aws.efs.</code><code class="sig-name descname">get_file_system</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">creation_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.efs.get_file_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about an Elastic File System (EFS) File System.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">file_system_id</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;fileSystemId&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">file_system_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">file_system_id</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
<span class="n">by_id</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">get_file_system</span><span class="p">(</span><span class="n">file_system_id</span><span class="o">=</span><span class="n">file_system_id</span><span class="p">)</span>
</pre></div>
</div>
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
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">mount_target_id</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;mountTargetId&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">mount_target_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">mount_target_id</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
<span class="n">by_id</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">efs</span><span class="o">.</span><span class="n">get_mount_target</span><span class="p">(</span><span class="n">mount_target_id</span><span class="o">=</span><span class="n">mount_target_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mount_target_id</strong> (<em>str</em>) – ID of the mount target that you want to have described</p>
</dd>
</dl>
</dd></dl>

</div>
