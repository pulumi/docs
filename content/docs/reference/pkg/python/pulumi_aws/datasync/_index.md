---
---

<div class="section" id="datasync">
<h1>datasync<a class="headerlink" href="#datasync" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.datasync"></span><dl class="class">
<dt id="pulumi_aws.datasync.Agent">
<em class="property">class </em><code class="descclassname">pulumi_aws.datasync.</code><code class="descname">Agent</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>activation_key=None</em>, <em>ip_address=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Agent resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Agent.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Agent.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Agent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DataSync Agent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Agent.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Agent.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Agent.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.EfsLocation">
<em class="property">class </em><code class="descclassname">pulumi_aws.datasync.</code><code class="descname">EfsLocation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ec2_config=None</em>, <em>efs_file_system_arn=None</em>, <em>subdirectory=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS DataSync EFS Location.</p>
<blockquote>
<div><strong>NOTE:</strong> The EFS File System must have a mounted EFS Mount Target before creating this resource.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ec2_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing EC2 configurations for connecting to the EFS File System.</li>
<li><strong>efs_file_system_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of EFS File System.</li>
<li><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Default <code class="docutils literal notranslate"><span class="pre">/</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.ec2_config">
<code class="descname">ec2_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.ec2_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing EC2 configurations for connecting to the EFS File System.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.efs_file_system_arn">
<code class="descname">efs_file_system_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.efs_file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of EFS File System.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.subdirectory">
<code class="descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdirectory to perform actions as source or destination. Default <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.EfsLocation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.EfsLocation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.NfsLocation">
<em class="property">class </em><code class="descclassname">pulumi_aws.datasync.</code><code class="descname">NfsLocation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>on_prem_config=None</em>, <em>server_hostname=None</em>, <em>subdirectory=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an NFS Location within AWS DataSync.</p>
<blockquote>
<div><strong>NOTE:</strong> The DataSync Agents must be available before creating this resource.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>on_prem_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to the NFS File System.</li>
<li><strong>server_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.</li>
<li><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.on_prem_config">
<code class="descname">on_prem_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.on_prem_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing information for connecting to the NFS File System.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.server_hostname">
<code class="descname">server_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.server_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.subdirectory">
<code class="descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.NfsLocation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.NfsLocation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.S3Location">
<em class="property">class </em><code class="descclassname">pulumi_aws.datasync.</code><code class="descname">S3Location</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>s3_bucket_arn=None</em>, <em>s3_config=None</em>, <em>subdirectory=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an S3 Location within AWS DataSync.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>s3_bucket_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the S3 Bucket.</li>
<li><strong>s3_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to S3.</li>
<li><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to perform actions as source or destination.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.s3_bucket_arn">
<code class="descname">s3_bucket_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.s3_bucket_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the S3 Bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.s3_config">
<code class="descname">s3_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.s3_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing information for connecting to S3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.subdirectory">
<code class="descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix to perform actions as source or destination.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.S3Location.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.S3Location.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Task">
<em class="property">class </em><code class="descclassname">pulumi_aws.datasync.</code><code class="descname">Task</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cloudwatch_log_group_arn=None</em>, <em>destination_location_arn=None</em>, <em>name=None</em>, <em>options=None</em>, <em>source_location_arn=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Task resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.</li>
<li><strong>destination_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of destination DataSync Location.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Task.</li>
<li><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.</li>
<li><strong>source_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of source DataSync Location.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Task.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.cloudwatch_log_group_arn">
<code class="descname">cloudwatch_log_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.cloudwatch_log_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.destination_location_arn">
<code class="descname">destination_location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.destination_location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of destination DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DataSync Task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.options">
<code class="descname">options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.source_location_arn">
<code class="descname">source_location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.source_location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of source DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Task.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Task.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Task.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
