---
title: Module directoryservice
title_tag: Module directoryservice | Package pulumi_aws | Python SDK
linktitle: directoryservice
notitle: true
---

<div class="section" id="directoryservice">
<h1>directoryservice<a class="headerlink" href="#directoryservice" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.directoryservice"></span><dl class="class">
<dt id="pulumi_aws.directoryservice.AwaitableGetDirectoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">AwaitableGetDirectoryResult</code><span class="sig-paren">(</span><em class="sig-param">access_url=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">connect_settings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">dns_ip_addresses=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">enable_sso=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpc_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.AwaitableGetDirectoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.directoryservice.ConditionalForwader">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">ConditionalForwader</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">dns_ips=None</em>, <em class="sig-param">remote_domain_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_conditional_forwarder.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_conditional_forwarder.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</p></li>
<li><p><strong>dns_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of forwarder IP addresses.</p></li>
<li><p><strong>remote_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the remote domain for which forwarders will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.directory_id">
<code class="sig-name descname">directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.dns_ips">
<code class="sig-name descname">dns_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.dns_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of forwarder IP addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.remote_domain_name">
<code class="sig-name descname">remote_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.remote_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the remote domain for which forwarders will be used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">dns_ips=None</em>, <em class="sig-param">remote_domain_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConditionalForwader resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</p></li>
<li><p><strong>dns_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of forwarder IP addresses.</p></li>
<li><p><strong>remote_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the remote domain for which forwarders will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.ConditionalForwader.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.Directory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">Directory</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">connect_settings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">enable_sso=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpc_settings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Simple or Managed Microsoft directory in AWS Directory Service.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the password and customer username will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_directory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_directory.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias for the directory (must be unique amongst all aliases in AWS). Required for <code class="docutils literal notranslate"><span class="pre">enable_sso</span></code>.</p></li>
<li><p><strong>connect_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Connector related information about the directory. Fields documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description for the directory.</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MicrosoftAD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>). Defaults to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> (applies to MicrosoftAD type only).</p></li>
<li><p><strong>enable_sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable single-sign on for the directory. Requires <code class="docutils literal notranslate"><span class="pre">alias</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name for the directory, such as <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code></p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the directory administrator or connector user.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the directory, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the directory (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code> are accepted values).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code> are accepted values). Defaults to <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>.</p></li>
<li><p><strong>vpc_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – VPC related information about the directory. Fields documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connect_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customerDnsIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The DNS IP addresses of the domain to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customerUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username corresponding to the password provided.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
<p>The <strong>vpc_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.access_url">
<code class="sig-name descname">access_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.access_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The access URL for the directory, such as <code class="docutils literal notranslate"><span class="pre">http://alias.awsapps.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias for the directory (must be unique amongst all aliases in AWS). Required for <code class="docutils literal notranslate"><span class="pre">enable_sso</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.connect_settings">
<code class="sig-name descname">connect_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.connect_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Connector related information about the directory. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customerDnsIps</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The DNS IP addresses of the domain to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customerUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username corresponding to the password provided.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description for the directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.dns_ip_addresses">
<code class="sig-name descname">dns_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.dns_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses of the DNS servers for the directory or connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.edition">
<code class="sig-name descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The MicrosoftAD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>). Defaults to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> (applies to MicrosoftAD type only).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.enable_sso">
<code class="sig-name descname">enable_sso</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.enable_sso" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable single-sign on for the directory. Requires <code class="docutils literal notranslate"><span class="pre">alias</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name for the directory, such as <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the directory administrator or connector user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group created by the directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the directory, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the directory (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code> are accepted values).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code> are accepted values). Defaults to <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.vpc_settings">
<code class="sig-name descname">vpc_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.vpc_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC related information about the directory. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.Directory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_url=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">connect_settings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_ip_addresses=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">enable_sso=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpc_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Directory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access URL for the directory, such as <code class="docutils literal notranslate"><span class="pre">http://alias.awsapps.com</span></code>.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias for the directory (must be unique amongst all aliases in AWS). Required for <code class="docutils literal notranslate"><span class="pre">enable_sso</span></code>.</p></li>
<li><p><strong>connect_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Connector related information about the directory. Fields documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description for the directory.</p></li>
<li><p><strong>dns_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses of the DNS servers for the directory or connector.</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MicrosoftAD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>). Defaults to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> (applies to MicrosoftAD type only).</p></li>
<li><p><strong>enable_sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable single-sign on for the directory. Requires <code class="docutils literal notranslate"><span class="pre">alias</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name for the directory, such as <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code></p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the directory administrator or connector user.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group created by the directory.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the directory, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the directory (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code> are accepted values).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code> are accepted values). Defaults to <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>.</p></li>
<li><p><strong>vpc_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – VPC related information about the directory. Fields documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connect_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customerDnsIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The DNS IP addresses of the domain to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customerUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username corresponding to the password provided.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
<p>The <strong>vpc_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier of the VPC that the directory is in.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.Directory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.Directory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.GetDirectoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">GetDirectoryResult</code><span class="sig-paren">(</span><em class="sig-param">access_url=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">connect_settings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">dns_ip_addresses=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">enable_sso=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpc_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDirectory.</p>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.access_url">
<code class="sig-name descname">access_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.access_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The access URL for the directory/connector, such as <a class="reference external" href="http://alias.awsapps.com">http://alias.awsapps.com</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias for the directory/connector, such as <code class="docutils literal notranslate"><span class="pre">d-991708b282.awsapps.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description for the directory/connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.dns_ip_addresses">
<code class="sig-name descname">dns_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.dns_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses of the DNS servers for the directory/connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.edition">
<code class="sig-name descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>(for <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code>) The Microsoft AD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.enable_sso">
<code class="sig-name descname">enable_sso</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.enable_sso" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory/connector single-sign on status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name for the directory/connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group created by the directory/connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the directory/connector, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>(for <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code> and <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code>) The size of the directory/connector (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the directory/connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.GetDirectoryResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.GetDirectoryResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code>).</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.directoryservice.LogService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">LogService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">log_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Log subscription for AWS Directory Service that pushes logs to cloudwatch.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_log_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_log_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.LogService.directory_id">
<code class="sig-name descname">directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.LogService.log_group_name">
<code class="sig-name descname">log_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.log_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.LogService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">directory_id=None</em>, <em class="sig-param">log_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.LogService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.LogService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.get_directory">
<code class="sig-prename descclassname">pulumi_aws.directoryservice.</code><code class="sig-name descname">get_directory</code><span class="sig-paren">(</span><em class="sig-param">directory_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.get_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Get attributes of AWS Directory Service directory (SimpleAD, Managed AD, AD Connector). It’s especially useful to refer AWS Managed AD or on-premise AD in AD Connector configuration.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/directory_service_directory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/directory_service_directory.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>directory_id</strong> (<em>str</em>) – The ID of the directory.</p>
</dd>
</dl>
</dd></dl>

</div>
