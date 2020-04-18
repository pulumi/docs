---
title: Module transfer
title_tag: Module transfer | Package pulumi_aws | Python SDK
linktitle: transfer
notitle: true
---

<div class="section" id="transfer">
<h1>transfer<a class="headerlink" href="#transfer" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.transfer"></span><dl class="class">
<dt id="pulumi_aws.transfer.AwaitableGetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">AwaitableGetServerResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identity_provider_type=None</em>, <em class="sig-param">invocation_role=None</em>, <em class="sig-param">logging_role=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.AwaitableGetServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.transfer.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identity_provider_type=None</em>, <em class="sig-param">invocation_role=None</em>, <em class="sig-param">logging_role=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer Server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678.server.transfer.REGION.amazonaws.com</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.identity_provider_type">
<code class="sig-name descname">identity_provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.identity_provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.invocation_role">
<code class="sig-name descname">invocation_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.invocation_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.logging_role">
<code class="sig-name descname">logging_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.logging_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.GetServerResult.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.GetServerResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.transfer.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_details=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">host_key=None</em>, <em class="sig-param">identity_provider_type=None</em>, <em class="sig-param">invocation_role=None</em>, <em class="sig-param">logging_role=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer Server resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of endpoint that you want your SFTP server connect to. If you connect to a <code class="docutils literal notranslate"><span class="pre">VPC_ENDPOINT</span></code>, your SFTP server isn’t accessible over the public internet. If you want to connect your SFTP server via public internet, set <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>host_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RSA private key (e.g. as generated by the <code class="docutils literal notranslate"><span class="pre">ssh-keygen</span> <span class="pre">-N</span> <span class="pre">&quot;&quot;</span> <span class="pre">-f</span> <span class="pre">my-new-server-key</span></code> command).</p></li>
<li><p><strong>identity_provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p></li>
<li><p><strong>invocation_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p></li>
<li><p><strong>logging_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the VPC endpoint.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer Server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678.server.transfer.REGION.amazonaws.com</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint_details">
<code class="sig-name descname">endpoint_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the VPC endpoint.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.endpoint_type">
<code class="sig-name descname">endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of endpoint that you want your SFTP server connect to. If you connect to a <code class="docutils literal notranslate"><span class="pre">VPC_ENDPOINT</span></code>, your SFTP server isn’t accessible over the public internet. If you want to connect your SFTP server via public internet, set <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.host_key">
<code class="sig-name descname">host_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.host_key" title="Permalink to this definition">¶</a></dt>
<dd><p>RSA private key (e.g. as generated by the <code class="docutils literal notranslate"><span class="pre">ssh-keygen</span> <span class="pre">-N</span> <span class="pre">&quot;&quot;</span> <span class="pre">-f</span> <span class="pre">my-new-server-key</span></code> command).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.host_key_fingerprint">
<code class="sig-name descname">host_key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.host_key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>This value contains the message-digest algorithm (MD5) hash of the server’s host key. This value is equivalent to the output of the <code class="docutils literal notranslate"><span class="pre">ssh-keygen</span> <span class="pre">-l</span> <span class="pre">-E</span> <span class="pre">md5</span> <span class="pre">-f</span> <span class="pre">my-new-server-key</span></code> command.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.identity_provider_type">
<code class="sig-name descname">identity_provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.identity_provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.invocation_role">
<code class="sig-name descname">invocation_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.invocation_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.logging_role">
<code class="sig-name descname">logging_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.logging_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.Server.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.Server.url" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">endpoint_details=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">host_key=None</em>, <em class="sig-param">host_key_fingerprint=None</em>, <em class="sig-param">identity_provider_type=None</em>, <em class="sig-param">invocation_role=None</em>, <em class="sig-param">logging_role=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of Transfer Server</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678.server.transfer.REGION.amazonaws.com</span></code>)</p></li>
<li><p><strong>endpoint_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of endpoint that you want your SFTP server connect to. If you connect to a <code class="docutils literal notranslate"><span class="pre">VPC_ENDPOINT</span></code>, your SFTP server isn’t accessible over the public internet. If you want to connect your SFTP server via public internet, set <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code>.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>host_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RSA private key (e.g. as generated by the <code class="docutils literal notranslate"><span class="pre">ssh-keygen</span> <span class="pre">-N</span> <span class="pre">&quot;&quot;</span> <span class="pre">-f</span> <span class="pre">my-new-server-key</span></code> command).</p></li>
<li><p><strong>host_key_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This value contains the message-digest algorithm (MD5) hash of the server’s host key. This value is equivalent to the output of the <code class="docutils literal notranslate"><span class="pre">ssh-keygen</span> <span class="pre">-l</span> <span class="pre">-E</span> <span class="pre">md5</span> <span class="pre">-f</span> <span class="pre">my-new-server-key</span></code> command.</p></li>
<li><p><strong>identity_provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of authentication enabled for this service. The default value is <code class="docutils literal notranslate"><span class="pre">SERVICE_MANAGED</span></code>, which allows you to store and access SFTP user credentials within the service. <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code> indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.</p></li>
<li><p><strong>invocation_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p></li>
<li><p><strong>logging_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>URL of the service endpoint used to authenticate users with an <code class="docutils literal notranslate"><span class="pre">identity_provider_type</span></code> of <code class="docutils literal notranslate"><span class="pre">API_GATEWAY</span></code>.</p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the VPC endpoint.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">body=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User SSH Key resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key portion of an SSH key pair.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user account that is assigned to one or more servers.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.body">
<code class="sig-name descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.body" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key portion of an SSH key pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.server_id">
<code class="sig-name descname">server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.SshKey.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.SshKey.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user account that is assigned to one or more servers.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">body=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key portion of an SSH key pair.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user account that is assigned to one or more servers.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">home_directory=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the <cite>``transfer.SshKey`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html">https://www.terraform.io/docs/providers/aws/r/transfer_ssh_key.html</a>&gt;`_.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>home_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.  The first item in the path is the name of the home bucket (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code> in the policy) and the rest is the home directory (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code> in the policy). For example, <code class="docutils literal notranslate"><span class="pre">/example-bucket-1234/username</span></code> would set the home bucket to <code class="docutils literal notranslate"><span class="pre">example-bucket-1234</span></code> and the home directory to <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <code class="docutils literal notranslate"><span class="pre">${Transfer:UserName}</span></code>, <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code>, and <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code>. These are evaluated on-the-fly when navigating the bucket.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used for log in to your SFTP server.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.transfer.User.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of Transfer User</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.home_directory">
<code class="sig-name descname">home_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.home_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.  The first item in the path is the name of the home bucket (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code> in the policy) and the rest is the home directory (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code> in the policy). For example, <code class="docutils literal notranslate"><span class="pre">/example-bucket-1234/username</span></code> would set the home bucket to <code class="docutils literal notranslate"><span class="pre">example-bucket-1234</span></code> and the home directory to <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <code class="docutils literal notranslate"><span class="pre">${Transfer:UserName}</span></code>, <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code>, and <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code>. These are evaluated on-the-fly when navigating the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.server_id">
<code class="sig-name descname">server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.transfer.User.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.transfer.User.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used for log in to your SFTP server.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">home_directory=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">server_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of Transfer User</p></li>
<li><p><strong>home_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.  The first item in the path is the name of the home bucket (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code> in the policy) and the rest is the home directory (accessible as <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code> in the policy). For example, <code class="docutils literal notranslate"><span class="pre">/example-bucket-1234/username</span></code> would set the home bucket to <code class="docutils literal notranslate"><span class="pre">example-bucket-1234</span></code> and the home directory to <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include <code class="docutils literal notranslate"><span class="pre">${Transfer:UserName}</span></code>, <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeDirectory}</span></code>, and <code class="docutils literal notranslate"><span class="pre">${Transfer:HomeBucket}</span></code>. These are evaluated on-the-fly when navigating the bucket.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Server ID of the Transfer Server (e.g. <code class="docutils literal notranslate"><span class="pre">s-12345678</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used for log in to your SFTP server.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.transfer.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.transfer.get_server">
<code class="sig-prename descclassname">pulumi_aws.transfer.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param">server_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.transfer.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of an AWS Transfer Server for use in other
resources.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>server_id</strong> (<em>str</em>) – ID for an SFTP server.</p>
</dd>
</dl>
</dd></dl>

</div>
