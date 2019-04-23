<div class="section" id="module-pulumi_aws.secretsmanager">
<span id="secretsmanager"></span><h1>secretsmanager<a class="headerlink" href="#module-pulumi_aws.secretsmanager" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.secretsmanager.GetSecretResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">GetSecretResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>description=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>policy=None</em>, <em>rotation_enabled=None</em>, <em>rotation_lambda_arn=None</em>, <em>rotation_rules=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource-based policy document that’s attached to the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.rotation_enabled">
<code class="descname">rotation_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.rotation_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether rotation is enabled or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.rotation_lambda_arn">
<code class="descname">rotation_lambda_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.rotation_lambda_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.rotation_rules">
<code class="descname">rotation_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.rotation_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rotation rules if rotation is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">GetSecretVersionResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>secret_binary=None</em>, <em>secret_string=None</em>, <em>version_id=None</em>, <em>version_stages=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecretVersion.</p>
<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult.secret_binary">
<code class="descname">secret_binary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult.secret_binary" title="Permalink to this definition">¶</a></dt>
<dd><p>The decrypted part of the protected secret information that was originally provided as a binary. Base64 encoded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult.secret_string">
<code class="descname">secret_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult.secret_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The decrypted part of the protected secret information that was originally provided as a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult.version_id">
<code class="descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of this version of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.GetSecretVersionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.GetSecretVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.secretsmanager.Secret">
<em class="property">class </em><code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">Secret</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>recovery_window_in_days=None</em>, <em>rotation_lambda_arn=None</em>, <em>rotation_rules=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the <cite>``aws_secretsmanager_secret_version`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html">https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the secret.</li>
<li><strong>kms_key*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don’t specify this value, then Secrets Manager defaults to using the AWS account’s default CMK (the one named <code class="docutils literal notranslate"><span class="pre">aws/secretsmanager</span></code>). If the default KMS CMK with that name doesn’t yet exist, then AWS Secrets Manager creates it for you automatically the first time.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: <cite>/*+=.&#64;-``Conflicts with`</cite>name_prefix<a href="#id3"><span class="problematic" id="id4">``</span></a>.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with``name<a href="#id5"><span class="problematic" id="id6">``</span></a>.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid JSON document representing a [resource policy](<a class="reference external" href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html">https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html</a>). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>).</li>
<li><strong>recovery_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be``0<code class="docutils literal notranslate"><span class="pre">to</span> <span class="pre">force</span> <span class="pre">deletion</span> <span class="pre">without</span> <span class="pre">recovery</span> <span class="pre">or</span> <span class="pre">range</span> <span class="pre">from</span></code>7<code class="docutils literal notranslate"><span class="pre">to</span></code>30<code class="docutils literal notranslate"><span class="pre">days.</span> <span class="pre">The</span> <span class="pre">default</span> <span class="pre">value</span> <span class="pre">is</span></code>30`.</li>
<li><strong>rotation_lambda_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ARN of the Lambda function that can rotate the secret.</li>
<li><strong>rotation_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A structure that defines the rotation configuration for this secret. Defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a key-value map of user-defined tags that are attached to the secret.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don’t specify this value, then Secrets Manager defaults to using the AWS account’s default CMK (the one named <code class="docutils literal notranslate"><span class="pre">aws/secretsmanager</span></code>). If the default KMS CMK with that name doesn’t yet exist, then AWS Secrets Manager creates it for you automatically the first time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: <code class="docutils literal notranslate"><span class="pre">/_+=.&#64;-</span></code> Conflicts with <code class="docutils literal notranslate"><span class="pre">name_prefix</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid JSON document representing a <a class="reference external" href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html">resource policy</a>. For more information about building AWS IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.recovery_window_in_days">
<code class="descname">recovery_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.recovery_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be <code class="docutils literal notranslate"><span class="pre">0</span></code> to force deletion without recovery or range from <code class="docutils literal notranslate"><span class="pre">7</span></code> to <code class="docutils literal notranslate"><span class="pre">30</span></code> days. The default value is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.rotation_enabled">
<code class="descname">rotation_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.rotation_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether automatic rotation is enabled for this secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.rotation_lambda_arn">
<code class="descname">rotation_lambda_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.rotation_lambda_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ARN of the Lambda function that can rotate the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.rotation_rules">
<code class="descname">rotation_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.rotation_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure that defines the rotation configuration for this secret. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.Secret.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key-value map of user-defined tags that are attached to the secret.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.secretsmanager.Secret.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.secretsmanager.Secret.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.secretsmanager.SecretVersion">
<em class="property">class </em><code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">SecretVersion</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>secret_binary=None</em>, <em>secret_id=None</em>, <em>secret_string=None</em>, <em>version_stages=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the <cite>``aws_secretsmanager_secret`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret.html">https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret.html</a>&gt;`_.</p>
<blockquote>
<div><strong>NOTE:</strong> If the <code class="docutils literal notranslate"><span class="pre">AWSCURRENT</span></code> staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from Terraform unless the secret itself is deleted. Move the <code class="docutils literal notranslate"><span class="pre">AWSCURRENT</span></code> staging label before or after deleting this resource from Terraform to fully trigger version deprecation if necessary.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>secret_binary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.</li>
<li><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.</li>
<li><strong>secret_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.</li>
<li><strong>version_stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that’s already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label <code class="docutils literal notranslate"><span class="pre">AWSCURRENT</span></code> to this new version on creation.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.secret_binary">
<code class="descname">secret_binary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.secret_binary" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.secret_id">
<code class="descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.secret_string">
<code class="descname">secret_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.secret_string" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.version_id">
<code class="descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the version of the secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.secretsmanager.SecretVersion.version_stages">
<code class="descname">version_stages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.version_stages" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that’s already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label <code class="docutils literal notranslate"><span class="pre">AWSCURRENT</span></code> to this new version on creation.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.secretsmanager.SecretVersion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.secretsmanager.SecretVersion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.SecretVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.secretsmanager.get_secret">
<code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">get_secret</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the <cite>``aws_secretsmanager_secret_version`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version.html">https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version.html</a>&gt;`_.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.secretsmanager.get_secret_version">
<code class="descclassname">pulumi_aws.secretsmanager.</code><code class="descname">get_secret_version</code><span class="sig-paren">(</span><em>secret_id=None</em>, <em>version_id=None</em>, <em>version_stage=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.secretsmanager.get_secret_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Secrets Manager secret version, including its secret value. To retrieve secret metadata, see the <cite>``aws_secretsmanager_secret`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret.html">https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret.html</a>&gt;`_.</p>
</dd></dl>

</div>
