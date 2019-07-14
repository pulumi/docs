---
---

<div class="section" id="directoryservice">
<h1>directoryservice<a class="headerlink" href="#directoryservice" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.directoryservice"></span><dl class="class">
<dt id="pulumi_aws.directoryservice.ConditionalForwader">
<em class="property">class </em><code class="descclassname">pulumi_aws.directoryservice.</code><code class="descname">ConditionalForwader</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>directory_id=None</em>, <em>dns_ips=None</em>, <em>remote_domain_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</li>
<li><strong>dns_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of forwarder IP addresses.</li>
<li><strong>remote_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the remote domain for which forwarders will be used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_conditional_forwarder.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_conditional_forwarder.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.directory_id">
<code class="descname">directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.dns_ips">
<code class="descname">dns_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.dns_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of forwarder IP addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.remote_domain_name">
<code class="descname">remote_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.remote_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the remote domain for which forwarders will be used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.ConditionalForwader.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.ConditionalForwader.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.ConditionalForwader.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.Directory">
<em class="property">class </em><code class="descclassname">pulumi_aws.directoryservice.</code><code class="descname">Directory</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>alias=None</em>, <em>connect_settings=None</em>, <em>description=None</em>, <em>edition=None</em>, <em>enable_sso=None</em>, <em>name=None</em>, <em>password=None</em>, <em>short_name=None</em>, <em>size=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>vpc_settings=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Simple or Managed Microsoft directory in AWS Directory Service.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the password and customer username will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias for the directory (must be unique amongst all aliases in AWS). Required for <code class="docutils literal notranslate"><span class="pre">enable_sso</span></code>.</li>
<li><strong>connect_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Connector related information about the directory. Fields documented below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description for the directory.</li>
<li><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MicrosoftAD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>). Defaults to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> (applies to MicrosoftAD type only).</li>
<li><strong>enable_sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable single-sign on for the directory. Requires <code class="docutils literal notranslate"><span class="pre">alias</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name for the directory, such as <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code></li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the directory administrator or connector user.</li>
<li><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the directory, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the directory (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code> are accepted values).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code> are accepted values). Defaults to <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>.</li>
<li><strong>vpc_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – VPC related information about the directory. Fields documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_directory.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_directory.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.access_url">
<code class="descname">access_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.access_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The access URL for the directory, such as <code class="docutils literal notranslate"><span class="pre">http://alias.awsapps.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.alias">
<code class="descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias for the directory (must be unique amongst all aliases in AWS). Required for <code class="docutils literal notranslate"><span class="pre">enable_sso</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.connect_settings">
<code class="descname">connect_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.connect_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Connector related information about the directory. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description for the directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.dns_ip_addresses">
<code class="descname">dns_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.dns_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses of the DNS servers for the directory or connector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.edition">
<code class="descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The MicrosoftAD edition (<code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code>). Defaults to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> (applies to MicrosoftAD type only).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.enable_sso">
<code class="descname">enable_sso</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.enable_sso" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable single-sign on for the directory. Requires <code class="docutils literal notranslate"><span class="pre">alias</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name for the directory, such as <code class="docutils literal notranslate"><span class="pre">corp.example.com</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the directory administrator or connector user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group created by the directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.short_name">
<code class="descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the directory, such as <code class="docutils literal notranslate"><span class="pre">CORP</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the directory (<code class="docutils literal notranslate"><span class="pre">Small</span></code> or <code class="docutils literal notranslate"><span class="pre">Large</span></code> are accepted values).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The directory type (<code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>, <code class="docutils literal notranslate"><span class="pre">ADConnector</span></code> or <code class="docutils literal notranslate"><span class="pre">MicrosoftAD</span></code> are accepted values). Defaults to <code class="docutils literal notranslate"><span class="pre">SimpleAD</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.Directory.vpc_settings">
<code class="descname">vpc_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.vpc_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC related information about the directory. Fields documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.Directory.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.Directory.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.Directory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.LogService">
<em class="property">class </em><code class="descclassname">pulumi_aws.directoryservice.</code><code class="descname">LogService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>directory_id=None</em>, <em>log_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Log subscription for AWS Directory Service that pushes logs to cloudwatch.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of directory.</li>
<li><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_log_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_log_subscription.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.directoryservice.LogService.directory_id">
<code class="descname">directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directoryservice.LogService.log_group_name">
<code class="descname">log_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.log_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directoryservice.LogService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directoryservice.LogService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directoryservice.LogService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
