<div class="section" id="module-pulumi_aws.transfer">
<span id="transfer"></span><h1>transfer<a class="headerlink" href="#module-pulumi_aws.transfer" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.transfer.Server">
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">Server</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>force_destroy=None</em>, <em>identity_provider_type=None</em>, <em>invocation_role=None</em>, <em>logging_role=None</em>, <em>tags=None</em>, <em>url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer Server resource.</p>
<p><a href="#id1"><span class="problematic" id="id2">``</span></a><a href="#id3"><span class="problematic" id="id4">`</span></a>hcl
resource “aws_iam_role” “foo” {</p>
<blockquote>
<div><p>name = “tf-test-transfer-server-iam-role”</p>
<p>assume_role_policy = &lt;&lt;EOF</p>
</div></blockquote>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><p>{
“Effect”: “Allow”,
“Principal”: {</p>
<blockquote>
<div>“Service”: “transfer.amazonaws.com”</div></blockquote>
<p>},
“Action”: “sts:AssumeRole”
}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
EOF
}</p>
<dl class="docutils">
<dt>resource “aws_iam_role_policy” “foo” {</dt>
<dd>name = “tf-test-transfer-server-iam-policy-%s”
role = “${aws_iam_role.foo.id}”
policy = &lt;&lt;POLICY</dd>
</dl>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><p>{
“Sid”: “AllowFullAccesstoCloudWatchLogs”,
“Effect”: “Allow”,
“Action”: [</p>
<blockquote>
<div>“logs:<a href="#id5"><span class="problematic" id="id6">*</span></a>”</div></blockquote>
<p>],
“Resource”: “*”
}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
POLICY
}</p>
<dl class="docutils">
<dt>resource “aws_transfer_server” “foo” {</dt>
<dd><p class="first">identity_provider_type = “SERVICE_MANAGED”
logging_role = “${aws_iam_role.foo.arn}”</p>
<dl class="docutils">
<dt>tags {</dt>
<dd>NAME   = “tf-acc-test-transfer-server”
ENV    = “test”</dd>
</dl>
<p class="last">}</p>
</dd>
</dl>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <cite>false</cite>.</li>
<li><strong>identity_provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of authentication enabled for this service. The default value is <cite>SERVICE_MANAGED</cite>, which allows you to store and access SFTP user credentials within the service. <cite>API_GATEWAY</cite> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</li>
<li><strong>invocation_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <cite>identity_provider_type</cite> of <cite>API_GATEWAY</cite>.</li>
<li><strong>logging_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>URL of the service endpoint used to authenticate users with an <cite>identity_provider_type</cite> of <cite>API_GATEWAY</cite>.</li>
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
<dd><p>The endpoint of the Transfer Server (e.g. <cite>s-12345678.server.transfer.REGION.amazonaws.com</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.identity_provider_type">
<code class="descname">identity_provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.identity_provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of authentication enabled for this service. The default value is <cite>SERVICE_MANAGED</cite>, which allows you to store and access SFTP user credentials within the service. <cite>API_GATEWAY</cite> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.invocation_role">
<code class="descname">invocation_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.invocation_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <cite>identity_provider_type</cite> of <cite>API_GATEWAY</cite>.</p>
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
<li>URL of the service endpoint used to authenticate users with an <cite>identity_provider_type</cite> of <cite>API_GATEWAY</cite>.</li>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">SshKey</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>body=None</em>, <em>server_id=None</em>, <em>user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User SSH Key resource.</p>
<p><a href="#id7"><span class="problematic" id="id8">``</span></a><a href="#id9"><span class="problematic" id="id10">`</span></a>hcl
resource “aws_transfer_server” “foo” {</p>
<blockquote>
<div><p>identity_provider_type = “SERVICE_MANAGED”</p>
<dl class="docutils">
<dt>tags {</dt>
<dd>NAME     = “tf-acc-test-transfer-server”</dd>
</dl>
<p>}</p>
</div></blockquote>
<p>}</p>
<dl class="docutils">
<dt>resource “aws_iam_role” “foo” {</dt>
<dd><p class="first">name = “tf-test-transfer-user-iam-role-%s”</p>
<p class="last">assume_role_policy = &lt;&lt;EOF</p>
</dd>
</dl>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><p>{
“Effect”: “Allow”,
“Principal”: {</p>
<blockquote>
<div>“Service”: “transfer.amazonaws.com”</div></blockquote>
<p>},
“Action”: “sts:AssumeRole”
}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
EOF
}</p>
<dl class="docutils">
<dt>resource “aws_iam_role_policy” “foo” {</dt>
<dd>name = “tf-test-transfer-user-iam-policy-%s”
role = “${aws_iam_role.foo.id}”
policy = &lt;&lt;POLICY</dd>
</dl>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Sid”: “AllowFullAccesstoS3”,
“Effect”: “Allow”,
“Action”: [</p>
<blockquote>
<div>“s3:<a href="#id11"><span class="problematic" id="id12">*</span></a>”</div></blockquote>
<p class="last">],
“Resource”: “*”</p>
</dd>
</dl>
<p>}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
POLICY
}</p>
<dl class="docutils">
<dt>resource “aws_transfer_user” “foo” {</dt>
<dd><p class="first">server_id      = “${aws_transfer_server.foo.id}”
user_name      = “tftestuser”
role           = “${aws_iam_role.foo.arn}”</p>
<dl class="docutils">
<dt>tags {</dt>
<dd>NAME = “tftestuser”</dd>
</dl>
<p class="last">}</p>
</dd>
</dl>
<p>}</p>
<dl class="docutils">
<dt>resource “aws_transfer_ssh_key” “foo” {</dt>
<dd>server_id = “${aws_transfer_server.foo.id}”
user_name = “${aws_transfer_user.foo.user_name}”
body      = “ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 <a class="reference external" href="mailto:example&#37;&#52;&#48;example&#46;com">example<span>&#64;</span>example<span>&#46;</span>com</a>”</dd>
</dl>
<p>}</p>
<p><a href="#id13"><span class="problematic" id="id14">``</span></a><a href="#id15"><span class="problematic" id="id16">`</span></a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key portion of an SSH key pair.</li>
<li><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <cite>s-12345678</cite>)</li>
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
<dd><p>The Server ID of the Transfer Server (e.g. <cite>s-12345678</cite>)</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.transfer.</code><code class="descname">User</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>home_directory=None</em>, <em>policy=None</em>, <em>role=None</em>, <em>server_id=None</em>, <em>tags=None</em>, <em>user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the [<cite>aws_transfer_ssh_key</cite> resource](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html">https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html</a>).</p>
<p><a href="#id17"><span class="problematic" id="id18">``</span></a><a href="#id19"><span class="problematic" id="id20">`</span></a>hcl
resource “aws_transfer_server” “foo” {</p>
<blockquote>
<div><p>identity_provider_type = “SERVICE_MANAGED”</p>
<dl class="docutils">
<dt>tags {</dt>
<dd>NAME     = “tf-acc-test-transfer-server”</dd>
</dl>
<p>}</p>
</div></blockquote>
<p>}</p>
<dl class="docutils">
<dt>resource “aws_iam_role” “foo” {</dt>
<dd><p class="first">name = “tf-test-transfer-user-iam-role”</p>
<p class="last">assume_role_policy = &lt;&lt;EOF</p>
</dd>
</dl>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><p>{
“Effect”: “Allow”,
“Principal”: {</p>
<blockquote>
<div>“Service”: “transfer.amazonaws.com”</div></blockquote>
<p>},
“Action”: “sts:AssumeRole”
}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
EOF
}</p>
<dl class="docutils">
<dt>resource “aws_iam_role_policy” “foo” {</dt>
<dd>name = “tf-test-transfer-user-iam-policy”
role = “${aws_iam_role.foo.id}”
policy = &lt;&lt;POLICY</dd>
</dl>
<dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Version”: “2012-10-17”,
“Statement”: [</p>
<blockquote>
<div><dl class="docutils">
<dt>{</dt>
<dd><p class="first">“Sid”: “AllowFullAccesstoS3”,
“Effect”: “Allow”,
“Action”: [</p>
<blockquote>
<div>“s3:<a href="#id21"><span class="problematic" id="id22">*</span></a>”</div></blockquote>
<p class="last">],
“Resource”: “*”</p>
</dd>
</dl>
<p>}</p>
</div></blockquote>
<p class="last">]</p>
</dd>
</dl>
<p>}
POLICY
}</p>
<dl class="docutils">
<dt>resource “aws_transfer_user” “foo” {</dt>
<dd>server_id      = “${aws_transfer_server.foo.id}”
user_name      = “tftestuser”
role           = “${aws_iam_role.foo.arn}”</dd>
</dl>
<p>}</p>
<p><a href="#id23"><span class="problematic" id="id24">``</span></a><a href="#id25"><span class="problematic" id="id26">`</span></a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>home_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The landing directory (folder) for a user when they log in to the server using their SFTP client.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <cite>${Transfer:UserName}</cite>, <cite>${Transfer:HomeDirectory}</cite>, and <cite>${Transfer:HomeBucket}</cite>. Since the IAM variable syntax matches Terraform’s interpolation syntax, they must be escaped inside Terraform configuration strings (<cite>$${Transfer:UserName}</cite>).</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</li>
<li><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <cite>s-12345678</cite>)</li>
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
<dd><p>The landing directory (folder) for a user when they log in to the server using their SFTP client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <cite>${Transfer:UserName}</cite>, <cite>${Transfer:HomeDirectory}</cite>, and <cite>${Transfer:HomeBucket}</cite>. Since the IAM variable syntax matches Terraform’s interpolation syntax, they must be escaped inside Terraform configuration strings (<cite>$${Transfer:UserName}</cite>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.server_id">
<code class="descname">server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Server ID of the Transfer Server (e.g. <cite>s-12345678</cite>)</p>
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

</div>
