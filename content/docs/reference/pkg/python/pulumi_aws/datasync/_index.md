---
title: Module datasync
title_tag: Module datasync | Package pulumi_aws | Python SDK
linktitle: datasync
notitle: true
---

<div class="section" id="datasync">
<h1>datasync<a class="headerlink" href="#datasync" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.datasync"></span><dl class="class">
<dt id="pulumi_aws.datasync.Agent">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">Agent</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_key=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS DataSync Agent deployed on premises.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One of <code class="docutils literal notranslate"><span class="pre">activation_key</span></code> or <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> must be provided for resource creation (agent activation). Neither is required for resource import. If using <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>, this provider must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DataSync Agent activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>. If an <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> is provided instead, the provider will retrieve the <code class="docutils literal notranslate"><span class="pre">activation_key</span></code> as part of the resource creation.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. DataSync Agent must be accessible on port 80 from where the provider is running.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Agent.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Agent.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.activation_key">
<code class="sig-name descname">activation_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.activation_key" title="Permalink to this definition">¶</a></dt>
<dd><p>DataSync Agent activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>. If an <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> is provided instead, the provider will retrieve the <code class="docutils literal notranslate"><span class="pre">activation_key</span></code> as part of the resource creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Agent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. DataSync Agent must be accessible on port 80 from where the provider is running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DataSync Agent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Agent.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Agent.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Agent.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Agent.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_key=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Agent resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DataSync Agent activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>. If an <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> is provided instead, the provider will retrieve the <code class="docutils literal notranslate"><span class="pre">activation_key</span></code> as part of the resource creation.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Agent.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with <code class="docutils literal notranslate"><span class="pre">activation_key</span></code>. DataSync Agent must be accessible on port 80 from where the provider is running.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Agent.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Agent.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_agent.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Agent.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Agent.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Agent.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.EfsLocation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">EfsLocation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ec2_config=None</em>, <em class="sig-param">efs_file_system_arn=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS DataSync EFS Location.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The EFS File System must have a mounted EFS Mount Target before creating this resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ec2_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing EC2 configurations for connecting to the EFS File System.</p></li>
<li><p><strong>efs_file_system_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of EFS File System.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Default <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ec2_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the EC2 Security Groups that are associated with the EFS Mount Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the EC2 Subnet that is associated with the EFS Mount Target.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.ec2_config">
<code class="sig-name descname">ec2_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.ec2_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing EC2 configurations for connecting to the EFS File System.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupArns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Amazon Resource Names (ARNs) of the EC2 Security Groups that are associated with the EFS Mount Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the EC2 Subnet that is associated with the EFS Mount Target.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.efs_file_system_arn">
<code class="sig-name descname">efs_file_system_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.efs_file_system_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of EFS File System.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.subdirectory">
<code class="sig-name descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdirectory to perform actions as source or destination. Default <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.EfsLocation.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.EfsLocation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">ec2_config=None</em>, <em class="sig-param">efs_file_system_arn=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EfsLocation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Location.</p></li>
<li><p><strong>ec2_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing EC2 configurations for connecting to the EFS File System.</p></li>
<li><p><strong>efs_file_system_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of EFS File System.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Default <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ec2_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the EC2 Security Groups that are associated with the EFS Mount Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the EC2 Subnet that is associated with the EFS Mount Target.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_efs.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.EfsLocation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.EfsLocation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.EfsLocation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.LocationSmb">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">LocationSmb</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_arns=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">mount_options=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">server_hostname=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SMB Location within AWS DataSync.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The DataSync Agents must be available before creating this resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of DataSync Agent ARNs with which this location will be associated.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows domain the SMB server belongs to.</p></li>
<li><p><strong>mount_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing mount options used by DataSync to access the SMB Server. Can be <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, or <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user who can mount the share and has file permissions in the SMB.</p></li>
<li><p><strong>server_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user who can mount the share and has file and folder permissions in the SMB share.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mount_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, and <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_smb.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_smb.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.agent_arns">
<code class="sig-name descname">agent_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.agent_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DataSync Agent ARNs with which this location will be associated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Windows domain the SMB server belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.mount_options">
<code class="sig-name descname">mount_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.mount_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing mount options used by DataSync to access the SMB Server. Can be <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, or <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, and <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user who can mount the share and has file permissions in the SMB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.server_hostname">
<code class="sig-name descname">server_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.server_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.subdirectory">
<code class="sig-name descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.LocationSmb.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user who can mount the share and has file and folder permissions in the SMB share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.LocationSmb.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_arns=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">mount_options=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">server_hostname=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LocationSmb resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of DataSync Agent ARNs with which this location will be associated.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Location.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows domain the SMB server belongs to.</p></li>
<li><p><strong>mount_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing mount options used by DataSync to access the SMB Server. Can be <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, or <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user who can mount the share and has file permissions in the SMB.</p></li>
<li><p><strong>server_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user who can mount the share and has file and folder permissions in the SMB share.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mount_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">SMB2</span></code>, and <code class="docutils literal notranslate"><span class="pre">SMB3</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_smb.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_smb.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.LocationSmb.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.LocationSmb.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.LocationSmb.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.NfsLocation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">NfsLocation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">on_prem_config=None</em>, <em class="sig-param">server_hostname=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an NFS Location within AWS DataSync.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The DataSync Agents must be available before creating this resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>on_prem_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to the NFS File System.</p></li>
<li><p><strong>server_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>on_prem_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">agent_arns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.on_prem_config">
<code class="sig-name descname">on_prem_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.on_prem_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing information for connecting to the NFS File System.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">agent_arns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.server_hostname">
<code class="sig-name descname">server_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.server_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.subdirectory">
<code class="sig-name descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.NfsLocation.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.NfsLocation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">on_prem_config=None</em>, <em class="sig-param">server_hostname=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NfsLocation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Location.</p></li>
<li><p><strong>on_prem_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to the NFS File System.</p></li>
<li><p><strong>server_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdirectory to perform actions as source or destination. Should be exported by the NFS server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>on_prem_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">agent_arns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.NfsLocation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.NfsLocation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.NfsLocation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.S3Location">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">S3Location</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">s3_bucket_arn=None</em>, <em class="sig-param">s3_config=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an S3 Location within AWS DataSync.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>s3_bucket_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the S3 Bucket.</p></li>
<li><p><strong>s3_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to S3.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to perform actions as source or destination.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>s3_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketAccessRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.s3_bucket_arn">
<code class="sig-name descname">s3_bucket_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.s3_bucket_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the S3 Bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.s3_config">
<code class="sig-name descname">s3_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.s3_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing information for connecting to S3.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketAccessRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.subdirectory">
<code class="sig-name descname">subdirectory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.subdirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix to perform actions as source or destination.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.S3Location.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.S3Location.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.S3Location.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">s3_bucket_arn=None</em>, <em class="sig-param">s3_config=None</em>, <em class="sig-param">subdirectory=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing S3Location resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Location.</p></li>
<li><p><strong>s3_bucket_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the S3 Bucket.</p></li>
<li><p><strong>s3_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing information for connecting to S3.</p></li>
<li><p><strong>subdirectory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to perform actions as source or destination.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Location.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>s3_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketAccessRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_s3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.S3Location.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.S3Location.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.S3Location.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Task">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.datasync.</code><code class="sig-name descname">Task</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_log_group_arn=None</em>, <em class="sig-param">destination_location_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">options=None</em>, <em class="sig-param">source_location_arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.</p></li>
<li><p><strong>destination_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of destination DataSync Location.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Task.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.</p></li>
<li><p><strong>source_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of source DataSync Location.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Task.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">atime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, the DataSync Task attempts to preserve the original (that is, the version before sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase) <code class="docutils literal notranslate"><span class="pre">atime</span></code> attribute on all source files. Valid values: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to <code class="docutils literal notranslate"><span class="pre">1048576</span></code>. Value values: <code class="docutils literal notranslate"><span class="pre">-1</span></code> or greater. Default: <code class="docutils literal notranslate"><span class="pre">-1</span></code> (unlimited).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Group identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mtime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A file metadata that indicates the last time a file was modified (written to) before the sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase. Value values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">posixPermissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDeletedFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>, <code class="docutils literal notranslate"><span class="pre">REMOVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDevices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (ignore special devices).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DataSync Task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.cloudwatch_log_group_arn">
<code class="sig-name descname">cloudwatch_log_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.cloudwatch_log_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.destination_location_arn">
<code class="sig-name descname">destination_location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.destination_location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of destination DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DataSync Task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.options">
<code class="sig-name descname">options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">atime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, the DataSync Task attempts to preserve the original (that is, the version before sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase) <code class="docutils literal notranslate"><span class="pre">atime</span></code> attribute on all source files. Valid values: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to <code class="docutils literal notranslate"><span class="pre">1048576</span></code>. Value values: <code class="docutils literal notranslate"><span class="pre">-1</span></code> or greater. Default: <code class="docutils literal notranslate"><span class="pre">-1</span></code> (unlimited).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Group identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mtime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A file metadata that indicates the last time a file was modified (written to) before the sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase. Value values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">posixPermissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDeletedFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>, <code class="docutils literal notranslate"><span class="pre">REMOVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDevices</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (ignore special devices).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - User identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.source_location_arn">
<code class="sig-name descname">source_location_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.source_location_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of source DataSync Location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.datasync.Task.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.datasync.Task.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs of resource tags to assign to the DataSync Task.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Task.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cloudwatch_log_group_arn=None</em>, <em class="sig-param">destination_location_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">options=None</em>, <em class="sig-param">source_location_arn=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Task resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DataSync Task.</p></li>
<li><p><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.</p></li>
<li><p><strong>destination_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of destination DataSync Location.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DataSync Task.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.</p></li>
<li><p><strong>source_location_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of source DataSync Location.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value pairs of resource tags to assign to the DataSync Task.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">atime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, the DataSync Task attempts to preserve the original (that is, the version before sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase) <code class="docutils literal notranslate"><span class="pre">atime</span></code> attribute on all source files. Valid values: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">BEST_EFFORT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to <code class="docutils literal notranslate"><span class="pre">1048576</span></code>. Value values: <code class="docutils literal notranslate"><span class="pre">-1</span></code> or greater. Default: <code class="docutils literal notranslate"><span class="pre">-1</span></code> (unlimited).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Group identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mtime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A file metadata that indicates the last time a file was modified (written to) before the sync <code class="docutils literal notranslate"><span class="pre">PREPARING</span></code> phase. Value values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">posixPermissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDeletedFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>, <code class="docutils literal notranslate"><span class="pre">REMOVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveDevices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">PRESERVE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (ignore special devices).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - User identifier of the file’s owners. Valid values: <code class="docutils literal notranslate"><span class="pre">BOTH</span></code>, <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code>, <code class="docutils literal notranslate"><span class="pre">NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">INT_VALUE</span></code> (preserve integer value of the ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">POINT_IN_TIME_CONSISTENT</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.datasync.Task.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.datasync.Task.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.datasync.Task.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
