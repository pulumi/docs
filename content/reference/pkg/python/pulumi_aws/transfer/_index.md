---
---

<div class="section" id="module-pulumi_aws.transfer">
<span id="transfer"></span><h1>transfer<a class="headerlink" href="#module-pulumi_aws.transfer" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.transfer.GetServerResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">GetServerResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>endpoint=None</em>, <em>identity_provider_type=None</em>, <em>invocation_role=None</em>, <em>logging_role=None</em>, <em>server_id=None</em>, <em>url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer Server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678.server.transfer.REGION.amazonaws.com</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.identity_provider_type">
<code class="descname">identity_provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.identity_provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.invocation_role">
<code class="descname">invocation_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.invocation_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.logging_role">
<code class="descname">logging_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.logging_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.transfer.Server">
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">Server</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint_details=None</em>, <em>endpoint_type=None</em>, <em>force_destroy=None</em>, <em>identity_provider_type=None</em>, <em>invocation_role=None</em>, <em>logging_role=None</em>, <em>tags=None</em>, <em>url=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer Server resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoint_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.</li>
<li><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of endpoint that you want your SFTP server connect to. If you connect to a <code class="docutils literal notranslate"><span class="pre">VPC_ENDPOINT</span></code>, your SFTP server isn’t accessible over the public internet. If you want to connect your SFTP server via public internet, set <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>identity_provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</li>
<li><strong>invocation_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</li>
<li><strong>logging_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</li>
</ul>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer Server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678.server.transfer.REGION.amazonaws.com</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint_details">
<code class="descname">endpoint_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint_type">
<code class="descname">endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of endpoint that you want your SFTP server connect to. If you connect to a <code class="docutils literal notranslate"><span class="pre">VPC_ENDPOINT</span></code>, your SFTP server isn’t accessible over the public internet. If you want to connect your SFTP server via public internet, set <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.identity_provider_type">
<code class="descname">identity_provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.identity_provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.invocation_role">
<code class="descname">invocation_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.invocation_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.logging_role">
<code class="descname">logging_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.logging_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.url" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.Server.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.Server.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.SshKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">SshKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>body=None</em>, <em>server_id=None</em>, <em>user_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User SSH Key resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key portion of an SSH key pair.</li>
<li><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</li>
<li><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user account that is assigned to one or more servers.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.body" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key portion of an SSH key pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.server_id">
<code class="descname">server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.user_name">
<code class="descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user account that is assigned to one or more servers.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.SshKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.SshKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.User">
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>home_directory=None</em>, <em>policy=None</em>, <em>role=None</em>, <em>server_id=None</em>, <em>tags=None</em>, <em>user_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the <cite>``aws_transfer_ssh_key`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html">https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>home_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.  The first item in the path is the name of the home bucket (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code> in the policy) and the rest is the home directory (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code> in the policy). For example, <code class="docutils literal notranslate"><span class="pre">/example-bucket-1234/username</span></code> would set the home bucket to <code class="docutils literal notranslate"><span class="pre">example-bucket-1234</span></code> and the home directory to <code class="docutils literal notranslate"><span class="pre">username</span></code>.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <code class="docutils literal notranslate"><span class="pre">${Transfer:UserName}</span></code>, <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code>, and <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code>. Since the IAM variable syntax matches Terraform’s interpolation syntax, they must be escaped inside Terraform configuration strings (<code class="docutils literal notranslate"><span class="pre">$${Transfer:UserName}</span></code>).  These are evaluated on-the-fly when navigating the bucket.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</li>
<li><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used for log in to your SFTP server.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.transfer.User.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer User</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.home_directory">
<code class="descname">home_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.home_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.  The first item in the path is the name of the home bucket (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code> in the policy) and the rest is the home directory (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code> in the policy). For example, <code class="docutils literal notranslate"><span class="pre">/example-bucket-1234/username</span></code> would set the home bucket to <code class="docutils literal notranslate"><span class="pre">example-bucket-1234</span></code> and the home directory to <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <code class="docutils literal notranslate"><span class="pre">${Transfer:UserName}</span></code>, <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code>, and <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code>. Since the IAM variable syntax matches Terraform’s interpolation syntax, they must be escaped inside Terraform configuration strings (<code class="docutils literal notranslate"><span class="pre">$${Transfer:UserName}</span></code>).  These are evaluated on-the-fly when navigating the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.server_id">
<code class="descname">server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.user_name">
<code class="descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used for log in to your SFTP server.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.get_server">
<code class="descclassname">pulumi_aws.transfer.</code><code class="descname">get_server</code><span class="sig-paren">(</span><em>server_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of an AWS Transfer Server for use in other
resources.</p>
</dd></dl>

</div>
