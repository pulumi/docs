---
title: Module aws
title_tag: Module aws | Package pulumi_vault | Python SDK
linktitle: aws
notitle: true
---

<div class="section" id="aws">
<h1>aws<a class="headerlink" href="#aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.aws"></span><dl class="class">
<dt id="pulumi_vault.aws.AuthBackendCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendCert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_public_cert=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cert_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackendCert resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_public_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The  Base64 encoded AWS Public key required to
verify PKCS7 signature of the EC2 instance metadata. You can find this key in
the <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html">AWS
documentation</a>.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>cert_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the certificate.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either “pkcs7” or “identity”, indicating the type of
document which can be verified using the given certificate. Defaults to
“pkcs7”.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_cert.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendCert.aws_public_cert">
<code class="sig-name descname">aws_public_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.aws_public_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The  Base64 encoded AWS Public key required to
verify PKCS7 signature of the EC2 instance metadata. You can find this key in
the <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html">AWS
documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendCert.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendCert.cert_name">
<code class="sig-name descname">cert_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.cert_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendCert.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Either “pkcs7” or “identity”, indicating the type of
document which can be verified using the given certificate. Defaults to
“pkcs7”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_public_cert=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cert_name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_public_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The  Base64 encoded AWS Public key required to
verify PKCS7 signature of the EC2 instance metadata. You can find this key in
the <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html">AWS
documentation</a>.</p>
</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>cert_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the certificate.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either “pkcs7” or “identity”, indicating the type of
document which can be verified using the given certificate. Defaults to
“pkcs7”.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_cert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendClient">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendClient</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">ec2_endpoint=None</em>, <em class="sig-param">iam_endpoint=None</em>, <em class="sig-param">iam_server_id_header_value=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">sts_endpoint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackendClient resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS access key that Vault should use for the
auth backend.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>ec2_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making EC2 API
calls.</p></li>
<li><p><strong>iam_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making IAM API
calls.</p></li>
<li><p><strong>iam_server_id_header_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to require in the
<code class="docutils literal notranslate"><span class="pre">X-Vault-AWS-IAM-Server-ID</span></code> header as part of <code class="docutils literal notranslate"><span class="pre">GetCallerIdentity</span></code> requests
that are used in the IAM auth method.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS secret key that Vault should use for the
auth backend.</p></li>
<li><p><strong>sts_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making STS API
calls.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_client.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_client.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.access_key">
<code class="sig-name descname">access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS access key that Vault should use for the
auth backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.ec2_endpoint">
<code class="sig-name descname">ec2_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.ec2_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Override the URL Vault uses when making EC2 API
calls.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.iam_endpoint">
<code class="sig-name descname">iam_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.iam_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Override the URL Vault uses when making IAM API
calls.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.iam_server_id_header_value">
<code class="sig-name descname">iam_server_id_header_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.iam_server_id_header_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to require in the
<code class="docutils literal notranslate"><span class="pre">X-Vault-AWS-IAM-Server-ID</span></code> header as part of <code class="docutils literal notranslate"><span class="pre">GetCallerIdentity</span></code> requests
that are used in the IAM auth method.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.secret_key">
<code class="sig-name descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS secret key that Vault should use for the
auth backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendClient.sts_endpoint">
<code class="sig-name descname">sts_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.sts_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Override the URL Vault uses when making STS API
calls.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendClient.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">ec2_endpoint=None</em>, <em class="sig-param">iam_endpoint=None</em>, <em class="sig-param">iam_server_id_header_value=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">sts_endpoint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendClient resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS access key that Vault should use for the
auth backend.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>ec2_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making EC2 API
calls.</p></li>
<li><p><strong>iam_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making IAM API
calls.</p></li>
<li><p><strong>iam_server_id_header_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to require in the
<code class="docutils literal notranslate"><span class="pre">X-Vault-AWS-IAM-Server-ID</span></code> header as part of <code class="docutils literal notranslate"><span class="pre">GetCallerIdentity</span></code> requests
that are used in the IAM auth method.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS secret key that Vault should use for the
auth backend.</p></li>
<li><p><strong>sts_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Override the URL Vault uses when making STS API
calls.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_client.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_client.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendClient.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendClient.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendClient.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendIdentityWhitelist</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disable_periodic_tidy=None</em>, <em class="sig-param">safety_buffer=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the periodic tidying operation of the whitelisted identity entries.</p>
<p>For more information, see the
<a class="reference external" href="https://www.vaultproject.io/api/auth/aws/index.html#configure-identity-whitelist-tidy-operation">Vault docs</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the AWS backend being configured.</p></li>
<li><p><strong>disable_periodic_tidy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, disables the periodic
tidying of the identity-whitelist entries.</p></li>
<li><p><strong>safety_buffer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of extra time, in minutes, that must
have passed beyond the roletag expiration, before it is removed from the
backend storage.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_identity_whitelist.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_identity_whitelist.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the AWS backend being configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.disable_periodic_tidy">
<code class="sig-name descname">disable_periodic_tidy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.disable_periodic_tidy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, disables the periodic
tidying of the identity-whitelist entries.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.safety_buffer">
<code class="sig-name descname">safety_buffer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.safety_buffer" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of extra time, in minutes, that must
have passed beyond the roletag expiration, before it is removed from the
backend storage.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disable_periodic_tidy=None</em>, <em class="sig-param">safety_buffer=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendIdentityWhitelist resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the AWS backend being configured.</p></li>
<li><p><strong>disable_periodic_tidy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, disables the periodic
tidying of the identity-whitelist entries.</p></li>
<li><p><strong>safety_buffer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of extra time, in minutes, that must
have passed beyond the roletag expiration, before it is removed from the
backend storage.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_identity_whitelist.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_identity_whitelist.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendIdentityWhitelist.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendIdentityWhitelist.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendLogin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendLogin</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">iam_http_request_method=None</em>, <em class="sig-param">iam_request_body=None</em>, <em class="sig-param">iam_request_headers=None</em>, <em class="sig-param">iam_request_url=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">nonce=None</em>, <em class="sig-param">pkcs7=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">signature=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs into a Vault server using an AWS auth backend. Login can be
accomplished using a signed identity request from IAM or using ec2
instance metadata. For more information, see the <a class="reference external" href="https://www.vaultproject.io/docs/auth/aws.html">Vault
documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the AWS auth backend. Defaults to
‘aws’.</p></li>
<li><p><strong>iam_http_request_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method used in the signed IAM
request.</p></li>
<li><p><strong>iam_request_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded body of the signed
request.</p></li>
<li><p><strong>iam_request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded, JSON serialized
representation of the GetCallerIdentity HTTP request headers.</p></li>
<li><p><strong>iam_request_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded HTTP URL used in the signed
request.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded EC2 instance identity document to
authenticate with. Can be retrieved from the EC2 metadata server.</p></li>
<li><p><strong>nonce</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique nonce to be used for login requests. Can be
set to a user-specified value, or will contain the server-generated value
once a token is issued. EC2 instances can only acquire a single token until
the whitelist is tidied again unless they keep track of this nonce.</p></li>
<li><p><strong>pkcs7</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKCS#7 signature of the identity document to
authenticate with, with all newline characters removed. Can be retrieved from
the EC2 metadata server.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS auth backend role to create tokens
against.</p></li>
<li><p><strong>signature</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded SHA256 RSA signature of the
instance identity document to authenticate with, with all newline characters
removed. Can be retrieved from the EC2 metadata server.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_login.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_login.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.accessor">
<code class="sig-name descname">accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The token’s accessor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.auth_type">
<code class="sig-name descname">auth_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.auth_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication type used to generate this token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the AWS auth backend. Defaults to
‘aws’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.client_token">
<code class="sig-name descname">client_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.client_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token returned by Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.iam_http_request_method">
<code class="sig-name descname">iam_http_request_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.iam_http_request_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method used in the signed IAM
request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.iam_request_body">
<code class="sig-name descname">iam_request_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.iam_request_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded body of the signed
request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.iam_request_headers">
<code class="sig-name descname">iam_request_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.iam_request_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded, JSON serialized
representation of the GetCallerIdentity HTTP request headers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.iam_request_url">
<code class="sig-name descname">iam_request_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.iam_request_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded HTTP URL used in the signed
request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded EC2 instance identity document to
authenticate with. Can be retrieved from the EC2 metadata server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.lease_duration">
<code class="sig-name descname">lease_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.lease_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration in seconds the token will be valid, relative
to the time in <code class="docutils literal notranslate"><span class="pre">lease_start_time</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of information returned by the Vault server about the
authentication used to generate this token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.nonce">
<code class="sig-name descname">nonce</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.nonce" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique nonce to be used for login requests. Can be
set to a user-specified value, or will contain the server-generated value
once a token is issued. EC2 instances can only acquire a single token until
the whitelist is tidied again unless they keep track of this nonce.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.pkcs7">
<code class="sig-name descname">pkcs7</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.pkcs7" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKCS#7 signature of the identity document to
authenticate with, with all newline characters removed. Can be retrieved from
the EC2 metadata server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The Vault policies assigned to this token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.renewable">
<code class="sig-name descname">renewable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.renewable" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true if the token can be extended through renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AWS auth backend role to create tokens
against.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendLogin.signature">
<code class="sig-name descname">signature</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.signature" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded SHA256 RSA signature of the
instance identity document to authenticate with, with all newline characters
removed. Can be retrieved from the EC2 metadata server.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendLogin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessor=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">client_token=None</em>, <em class="sig-param">iam_http_request_method=None</em>, <em class="sig-param">iam_request_body=None</em>, <em class="sig-param">iam_request_headers=None</em>, <em class="sig-param">iam_request_url=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_start_time=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">nonce=None</em>, <em class="sig-param">pkcs7=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">renewable=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">signature=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendLogin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token’s accessor.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication type used to generate this token.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the AWS auth backend. Defaults to
‘aws’.</p></li>
<li><p><strong>client_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token returned by Vault.</p></li>
<li><p><strong>iam_http_request_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method used in the signed IAM
request.</p></li>
<li><p><strong>iam_request_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded body of the signed
request.</p></li>
<li><p><strong>iam_request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded, JSON serialized
representation of the GetCallerIdentity HTTP request headers.</p></li>
<li><p><strong>iam_request_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded HTTP URL used in the signed
request.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded EC2 instance identity document to
authenticate with. Can be retrieved from the EC2 metadata server.</p></li>
<li><p><strong>lease_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration in seconds the token will be valid, relative
to the time in <code class="docutils literal notranslate"><span class="pre">lease_start_time</span></code>.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of information returned by the Vault server about the
authentication used to generate this token.</p></li>
<li><p><strong>nonce</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique nonce to be used for login requests. Can be
set to a user-specified value, or will contain the server-generated value
once a token is issued. EC2 instances can only acquire a single token until
the whitelist is tidied again unless they keep track of this nonce.</p></li>
<li><p><strong>pkcs7</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKCS#7 signature of the identity document to
authenticate with, with all newline characters removed. Can be retrieved from
the EC2 metadata server.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Vault policies assigned to this token.</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if the token can be extended through renewal.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS auth backend role to create tokens
against.</p></li>
<li><p><strong>signature</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded SHA256 RSA signature of the
instance identity document to authenticate with, with all newline characters
removed. Can be retrieved from the EC2 metadata server.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_login.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_login.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendLogin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendLogin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendLogin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_instance_migration=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_account_ids=None</em>, <em class="sig-param">bound_ami_ids=None</em>, <em class="sig-param">bound_ec2_instance_ids=None</em>, <em class="sig-param">bound_iam_instance_profile_arns=None</em>, <em class="sig-param">bound_iam_principal_arns=None</em>, <em class="sig-param">bound_iam_role_arns=None</em>, <em class="sig-param">bound_regions=None</em>, <em class="sig-param">bound_subnet_ids=None</em>, <em class="sig-param">bound_vpc_ids=None</em>, <em class="sig-param">disallow_reauthentication=None</em>, <em class="sig-param">inferred_aws_region=None</em>, <em class="sig-param">inferred_entity_type=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">resolve_aws_unique_ids=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">role_tag=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/aws.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_instance_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, allows migration of
the underlying instance where the client resides.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The auth type permitted for this role. Valid choices
are <code class="docutils literal notranslate"><span class="pre">ec2</span></code> and <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>bound_account_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they should be using the
account ID specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_ami_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that they should be using the AMI ID
specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_iam_instance_profile_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on
the EC2 instances that can perform the login operation that they must be
associated with an IAM instance profile ARN which has a prefix that matches
the value specified by this field. The value is prefix-matched as though it
were a glob ending in <code class="docutils literal notranslate"><span class="pre">*</span></code>. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_iam_principal_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines the IAM principal that
must be authenticated when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Wildcards are
supported at the end of the ARN.</p></li>
<li><p><strong>bound_iam_role_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they must match the IAM
role ARN specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that the region in their identity
document must match the one specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set
to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p></li>
<li><p><strong>bound_subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they be associated with
the subnet ID that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p></li>
<li><p><strong>bound_vpc_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that they be associated with the VPC ID
that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to
<code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p></li>
<li><p><strong>disallow_reauthentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – IF set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, only allows a
single token to be granted per instance ID. This can only be set when
<code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code>.</p></li>
<li><p><strong>inferred_aws_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set, this
is the region to search for the inferred entities. Required if
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set. This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>inferred_entity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, instructs Vault to turn on
inferencing. The only valid value is <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>, which instructs Vault to
infer that the role comes from an EC2 instance in an IAM instance profile.
This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>resolve_aws_unique_ids</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arns</span></code> are resolved to <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids">AWS Unique
IDs</a>
for the bound principal ARN. This field is ignored when a
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arn</span></code> ends in a wildcard. Resolving to unique IDs more
closely mimics the behavior of AWS services in that if an IAM user or role is
deleted and a new one is recreated with the same name, those new users or
roles won’t get access to roles in Vault that were permissioned to the prior
principals of the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Once set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this cannot be changed to <code class="docutils literal notranslate"><span class="pre">false</span></code> without recreating the role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>role_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, enable role tags for this role. The value set
for this field should be the key of the tag on the EC2 instance. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.allow_instance_migration">
<code class="sig-name descname">allow_instance_migration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.allow_instance_migration" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, allows migration of
the underlying instance where the client resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.auth_type">
<code class="sig-name descname">auth_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.auth_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The auth type permitted for this role. Valid choices
are <code class="docutils literal notranslate"><span class="pre">ec2</span></code> and <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_account_ids">
<code class="sig-name descname">bound_account_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_account_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2
instances that can perform the login operation that they should be using the
account ID specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_ami_ids">
<code class="sig-name descname">bound_ami_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_ami_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2 instances
that can perform the login operation that they should be using the AMI ID
specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_iam_instance_profile_arns">
<code class="sig-name descname">bound_iam_instance_profile_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_iam_instance_profile_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on
the EC2 instances that can perform the login operation that they must be
associated with an IAM instance profile ARN which has a prefix that matches
the value specified by this field. The value is prefix-matched as though it
were a glob ending in <code class="docutils literal notranslate"><span class="pre">*</span></code>. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_iam_principal_arns">
<code class="sig-name descname">bound_iam_principal_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_iam_principal_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines the IAM principal that
must be authenticated when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Wildcards are
supported at the end of the ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_iam_role_arns">
<code class="sig-name descname">bound_iam_role_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_iam_role_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2
instances that can perform the login operation that they must match the IAM
role ARN specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_regions">
<code class="sig-name descname">bound_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2 instances
that can perform the login operation that the region in their identity
document must match the one specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set
to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_subnet_ids">
<code class="sig-name descname">bound_subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2
instances that can perform the login operation that they be associated with
the subnet ID that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.bound_vpc_ids">
<code class="sig-name descname">bound_vpc_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.bound_vpc_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the EC2 instances
that can perform the login operation that they be associated with the VPC ID
that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to
<code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.disallow_reauthentication">
<code class="sig-name descname">disallow_reauthentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.disallow_reauthentication" title="Permalink to this definition">¶</a></dt>
<dd><p>IF set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, only allows a
single token to be granted per instance ID. This can only be set when
<code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.inferred_aws_region">
<code class="sig-name descname">inferred_aws_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.inferred_aws_region" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set, this
is the region to search for the inferred entities. Required if
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set. This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.inferred_entity_type">
<code class="sig-name descname">inferred_entity_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.inferred_entity_type" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, instructs Vault to turn on
inferencing. The only valid value is <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>, which instructs Vault to
infer that the role comes from an EC2 instance in an IAM instance profile.
This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.resolve_aws_unique_ids">
<code class="sig-name descname">resolve_aws_unique_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.resolve_aws_unique_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arns</span></code> are resolved to <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids">AWS Unique
IDs</a>
for the bound principal ARN. This field is ignored when a
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arn</span></code> ends in a wildcard. Resolving to unique IDs more
closely mimics the behavior of AWS services in that if an IAM user or role is
deleted and a new one is recreated with the same name, those new users or
roles won’t get access to roles in Vault that were permissioned to the prior
principals of the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Once set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this cannot be changed to <code class="docutils literal notranslate"><span class="pre">false</span></code> without recreating the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.role_tag">
<code class="sig-name descname">role_tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.role_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, enable role tags for this role. The value set
for this field should be the key of the tag on the EC2 instance. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_instance_migration=None</em>, <em class="sig-param">auth_type=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_account_ids=None</em>, <em class="sig-param">bound_ami_ids=None</em>, <em class="sig-param">bound_ec2_instance_ids=None</em>, <em class="sig-param">bound_iam_instance_profile_arns=None</em>, <em class="sig-param">bound_iam_principal_arns=None</em>, <em class="sig-param">bound_iam_role_arns=None</em>, <em class="sig-param">bound_regions=None</em>, <em class="sig-param">bound_subnet_ids=None</em>, <em class="sig-param">bound_vpc_ids=None</em>, <em class="sig-param">disallow_reauthentication=None</em>, <em class="sig-param">inferred_aws_region=None</em>, <em class="sig-param">inferred_entity_type=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">resolve_aws_unique_ids=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">role_tag=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_instance_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, allows migration of
the underlying instance where the client resides.</p></li>
<li><p><strong>auth_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The auth type permitted for this role. Valid choices
are <code class="docutils literal notranslate"><span class="pre">ec2</span></code> and <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>bound_account_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they should be using the
account ID specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_ami_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that they should be using the AMI ID
specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_iam_instance_profile_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on
the EC2 instances that can perform the login operation that they must be
associated with an IAM instance profile ARN which has a prefix that matches
the value specified by this field. The value is prefix-matched as though it
were a glob ending in <code class="docutils literal notranslate"><span class="pre">*</span></code>. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_iam_principal_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines the IAM principal that
must be authenticated when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>. Wildcards are
supported at the end of the ARN.</p></li>
<li><p><strong>bound_iam_role_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they must match the IAM
role ARN specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this constraint.</p></li>
<li><p><strong>bound_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that the region in their identity
document must match the one specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set
to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p></li>
<li><p><strong>bound_subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2
instances that can perform the login operation that they be associated with
the subnet ID that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p></li>
<li><p><strong>bound_vpc_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the EC2 instances
that can perform the login operation that they be associated with the VPC ID
that matches the value specified by this field. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> must be set to
<code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code> to use this
constraint.</p></li>
<li><p><strong>disallow_reauthentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – IF set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, only allows a
single token to be granted per instance ID. This can only be set when
<code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code>.</p></li>
<li><p><strong>inferred_aws_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set, this
is the region to search for the inferred entities. Required if
<code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> is set. This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>inferred_entity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, instructs Vault to turn on
inferencing. The only valid value is <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>, which instructs Vault to
infer that the role comes from an EC2 instance in an IAM instance profile.
This only applies when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">iam</span></code>.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>resolve_aws_unique_ids</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arns</span></code> are resolved to <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids">AWS Unique
IDs</a>
for the bound principal ARN. This field is ignored when a
<code class="docutils literal notranslate"><span class="pre">bound_iam_principal_arn</span></code> ends in a wildcard. Resolving to unique IDs more
closely mimics the behavior of AWS services in that if an IAM user or role is
deleted and a new one is recreated with the same name, those new users or
roles won’t get access to roles in Vault that were permissioned to the prior
principals of the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Once set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this cannot be changed to <code class="docutils literal notranslate"><span class="pre">false</span></code> without recreating the role.</p>
</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>role_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, enable role tags for this role. The value set
for this field should be the key of the tag on the EC2 instance. <code class="docutils literal notranslate"><span class="pre">auth_type</span></code>
must be set to <code class="docutils literal notranslate"><span class="pre">ec2</span></code> or <code class="docutils literal notranslate"><span class="pre">inferred_entity_type</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">ec2_instance</span></code>
to use this constraint.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRoleTag">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendRoleTag</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_instance_migration=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disallow_reauthentication=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads role tag information from an AWS auth backend in Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_instance_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, allows migration of the underlying instances where the client resides. Use with caution.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the AWS auth backend to
read role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s. Defaults to “aws”.</p></li>
<li><p><strong>disallow_reauthentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, only allows a single token to be granted per instance ID.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum TTL of the tokens issued using this role.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The policies to be associated with the tag. Must be a subset of the policies associated with the role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS auth backend role to read
role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role_tag.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role_tag.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.allow_instance_migration">
<code class="sig-name descname">allow_instance_migration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.allow_instance_migration" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, allows migration of the underlying instances where the client resides. Use with caution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the AWS auth backend to
read role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s. Defaults to “aws”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.disallow_reauthentication">
<code class="sig-name descname">disallow_reauthentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.disallow_reauthentication" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, only allows a single token to be granted per instance ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL of the tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The policies to be associated with the tag. Must be a subset of the policies associated with the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AWS auth backend role to read
role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.tag_key">
<code class="sig-name descname">tag_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.tag_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key of the role tag.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.tag_value">
<code class="sig-name descname">tag_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.tag_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to set the role key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_instance_migration=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disallow_reauthentication=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">tag_key=None</em>, <em class="sig-param">tag_value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRoleTag resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_instance_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, allows migration of the underlying instances where the client resides. Use with caution.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the AWS auth backend to
read role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s. Defaults to “aws”.</p></li>
<li><p><strong>disallow_reauthentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, only allows a single token to be granted per instance ID.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum TTL of the tokens issued using this role.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The policies to be associated with the tag. Must be a subset of the policies associated with the role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS auth backend role to read
role tags from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>tag_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key of the role tag.</p></li>
<li><p><strong>tag_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to set the role key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role_tag.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_role_tag.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRoleTag.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRoleTag.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoleTag.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendRoletagBlacklist</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disable_periodic_tidy=None</em>, <em class="sig-param">safety_buffer=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the periodic tidying operation of the blacklisted role tag entries.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.</p></li>
<li><p><strong>disable_periodic_tidy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, disables the periodic
tidying of the roletag blacklist entries. Defaults to false.</p></li>
<li><p><strong>safety_buffer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of extra time that must have passed
beyond the roletag expiration, before it is removed from the backend storage.
Defaults to 259,200 seconds, or 72 hours.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_roletag_blacklist.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_roletag_blacklist.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the AWS auth backend being configured was
mounted at.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.disable_periodic_tidy">
<code class="sig-name descname">disable_periodic_tidy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.disable_periodic_tidy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, disables the periodic
tidying of the roletag blacklist entries. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.safety_buffer">
<code class="sig-name descname">safety_buffer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.safety_buffer" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of extra time that must have passed
beyond the roletag expiration, before it is removed from the backend storage.
Defaults to 259,200 seconds, or 72 hours.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">disable_periodic_tidy=None</em>, <em class="sig-param">safety_buffer=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRoletagBlacklist resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.</p></li>
<li><p><strong>disable_periodic_tidy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, disables the periodic
tidying of the roletag blacklist entries. Defaults to false.</p></li>
<li><p><strong>safety_buffer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of extra time that must have passed
beyond the roletag expiration, before it is removed from the backend storage.
Defaults to 259,200 seconds, or 72 hours.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_roletag_blacklist.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_roletag_blacklist.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendRoletagBlacklist.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendRoletagBlacklist.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendStsRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AuthBackendStsRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">sts_role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackendStsRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID to configure the STS role for.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>sts_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The STS role to assume when verifying requests made
by EC2 instances in the account specified by <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_sts_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_sts_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendStsRole.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID to configure the STS role for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendStsRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.AuthBackendStsRole.sts_role">
<code class="sig-name descname">sts_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.sts_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The STS role to assume when verifying requests made
by EC2 instances in the account specified by <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendStsRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">sts_role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendStsRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID to configure the STS role for.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>sts_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The STS role to assume when verifying requests made
by EC2 instances in the account specified by <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_sts_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_auth_backend_sts_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.AuthBackendStsRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AuthBackendStsRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AuthBackendStsRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.AwaitableGetAccessCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">AwaitableGetAccessCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param">access_key=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_id=None</em>, <em class="sig-param">lease_renewable=None</em>, <em class="sig-param">lease_start_time=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">security_token=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.AwaitableGetAccessCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">GetAccessCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param">access_key=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_id=None</em>, <em class="sig-param">lease_renewable=None</em>, <em class="sig-param">lease_start_time=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">security_token=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessCredentials.</p>
<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.access_key">
<code class="sig-name descname">access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Access Key ID returned by Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.lease_duration">
<code class="sig-name descname">lease_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.lease_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the secret lease, in seconds relative
to the time the data was requested. Once this time has passed any plan
generated with this data may fail to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.lease_id">
<code class="sig-name descname">lease_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.lease_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The lease identifier assigned by Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.secret_key">
<code class="sig-name descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Secret Key returned by Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.security_token">
<code class="sig-name descname">security_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.security_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The STS token returned by Vault, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.GetAccessCredentialsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.GetAccessCredentialsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.aws.SecretBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">SecretBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackend resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Access Key ID this backend should use to
issue new credentials.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials
issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region for API calls. Defaults to <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Secret Key this backend should use to
issue new credentials.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.access_key">
<code class="sig-name descname">access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Access Key ID this backend should use to
issue new credentials.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.default_lease_ttl_seconds">
<code class="sig-name descname">default_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL for credentials
issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly description for this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.max_lease_ttl_seconds">
<code class="sig-name descname">max_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL that can be requested
for credentials issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region for API calls. Defaults to <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackend.secret_key">
<code class="sig-name descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Secret Key this backend should use to
issue new credentials.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.SecretBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Access Key ID this backend should use to
issue new credentials.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials
issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region for API calls. Defaults to <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Secret Key this backend should use to
issue new credentials.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.SecretBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.SecretBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">credential_type=None</em>, <em class="sig-param">default_sts_ttl=None</em>, <em class="sig-param">max_sts_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_arns=None</em>, <em class="sig-param">policy_document=None</em>, <em class="sig-param">role_arns=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>credential_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of credential to be used when
retrieving credentials from the role. Must be one of <code class="docutils literal notranslate"><span class="pre">iam_user</span></code>, <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code>, or
<code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>default_sts_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL in seconds for STS credentials.
When a TTL is not specified when STS credentials are requested,
and a default TTL is specified on the role,
then this default TTL will be used. Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is one of
<code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>max_sts_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max allowed TTL in seconds for STS credentials
(credentials TTL are capped to <code class="docutils literal notranslate"><span class="pre">max_sts_ttl</span></code>). Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is
one of <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend.
Must be unique within the backend.</p></li>
<li><p><strong>policy_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ARN for a pre-existing policy to associate
with this role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON-formatted policy to associate with this
role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p></li>
<li><p><strong>role_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the ARNs of the AWS roles this Vault role
is allowed to assume. Required when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> and
prohibited otherwise.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the AWS secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.credential_type">
<code class="sig-name descname">credential_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.credential_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of credential to be used when
retrieving credentials from the role. Must be one of <code class="docutils literal notranslate"><span class="pre">iam_user</span></code>, <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code>, or
<code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.default_sts_ttl">
<code class="sig-name descname">default_sts_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.default_sts_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL in seconds for STS credentials.
When a TTL is not specified when STS credentials are requested,
and a default TTL is specified on the role,
then this default TTL will be used. Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is one of
<code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.max_sts_ttl">
<code class="sig-name descname">max_sts_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.max_sts_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The max allowed TTL in seconds for STS credentials
(credentials TTL are capped to <code class="docutils literal notranslate"><span class="pre">max_sts_ttl</span></code>). Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is
one of <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify this role within the backend.
Must be unique within the backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.policy_arns">
<code class="sig-name descname">policy_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.policy_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for a pre-existing policy to associate
with this role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.policy_document">
<code class="sig-name descname">policy_document</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON-formatted policy to associate with this
role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.aws.SecretBackendRole.role_arns">
<code class="sig-name descname">role_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.role_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ARNs of the AWS roles this Vault role
is allowed to assume. Required when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> and
prohibited otherwise.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">credential_type=None</em>, <em class="sig-param">default_sts_ttl=None</em>, <em class="sig-param">max_sts_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_arns=None</em>, <em class="sig-param">policy_document=None</em>, <em class="sig-param">role_arns=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the AWS secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>credential_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of credential to be used when
retrieving credentials from the role. Must be one of <code class="docutils literal notranslate"><span class="pre">iam_user</span></code>, <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code>, or
<code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>default_sts_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL in seconds for STS credentials.
When a TTL is not specified when STS credentials are requested,
and a default TTL is specified on the role,
then this default TTL will be used. Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is one of
<code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>max_sts_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max allowed TTL in seconds for STS credentials
(credentials TTL are capped to <code class="docutils literal notranslate"><span class="pre">max_sts_ttl</span></code>). Valid only when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is
one of <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> or <code class="docutils literal notranslate"><span class="pre">federation_token</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend.
Must be unique within the backend.</p></li>
<li><p><strong>policy_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ARN for a pre-existing policy to associate
with this role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON-formatted policy to associate with this
role. Either <code class="docutils literal notranslate"><span class="pre">policy_document</span></code> or <code class="docutils literal notranslate"><span class="pre">policy_arns</span></code> must be specified.</p></li>
<li><p><strong>role_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the ARNs of the AWS roles this Vault role
is allowed to assume. Required when <code class="docutils literal notranslate"><span class="pre">credential_type</span></code> is <code class="docutils literal notranslate"><span class="pre">assumed_role</span></code> and
prohibited otherwise.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/aws_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.aws.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.aws.get_access_credentials">
<code class="sig-prename descclassname">pulumi_vault.aws.</code><code class="sig-name descname">get_access_credentials</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.aws.get_access_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backend</strong> (<em>str</em>) – The path to the AWS secret backend to
read credentials from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>role</strong> (<em>str</em>) – The name of the AWS secret backend role to read
credentials from, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The type of credentials to read. Defaults
to <code class="docutils literal notranslate"><span class="pre">&quot;creds&quot;</span></code>, which just returns an AWS Access Key ID and Secret
Key. Can also be set to <code class="docutils literal notranslate"><span class="pre">&quot;sts&quot;</span></code>, which will return a security token
in addition to the keys.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/aws_access_credentials.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/aws_access_credentials.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
