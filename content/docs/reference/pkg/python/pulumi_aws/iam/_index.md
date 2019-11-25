---
title: Module iam
linktitle: iam
notitle: true
---

<div class="section" id="iam">
<h1>iam<a class="headerlink" href="#iam" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.iam"></span><dl class="class">
<dt id="pulumi_aws.iam.AccessKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AccessKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a
keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key status to apply. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> and <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user to associate with this access key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.encrypted_secret">
<code class="sig-name descname">encrypted_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.encrypted_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The encrypted secret, base64 encoded.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The encrypted secret may be decrypted using the command line,
for example: <code class="docutils literal notranslate"><span class="pre">...</span> <span class="pre">|</span> <span class="pre">base64</span> <span class="pre">--decode</span> <span class="pre">|</span> <span class="pre">keybase</span> <span class="pre">pgp</span> <span class="pre">decrypt</span></code>.</p>
</div></blockquote>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.key_fingerprint">
<code class="sig-name descname">key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt
the secret</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.pgp_key">
<code class="sig-name descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a
keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.secret">
<code class="sig-name descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret access key. Note that this will be written
to the state file. Please supply a <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> instead, which will prevent the
secret from being stored in plain text</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.ses_smtp_password">
<code class="sig-name descname">ses_smtp_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.ses_smtp_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret access key converted into an SES SMTP
password by applying <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert">AWS’s documented conversion
algorithm</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The access key status to apply. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> and <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user to associate with this access key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccessKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encrypted_secret=None</em>, <em class="sig-param">key_fingerprint=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">ses_smtp_password=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encrypted_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encrypted secret, base64 encoded.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **NOTE:** The encrypted secret may be decrypted using the command line,
for example: `... | base64 --decode | keybase pgp decrypt`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the PGP key used to encrypt
the secret</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a
keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret access key. Note that this will be written
to the state file. Please supply a <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> instead, which will prevent the
secret from being stored in plain text</p></li>
<li><p><strong>ses_smtp_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The secret access key converted into an SES SMTP
password by applying <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert">AWS’s documented conversion
algorithm</a>.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key status to apply. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> and <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user to associate with this access key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccessKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccessKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountAlias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AccountAlias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_alias=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> There is only a single account alias per AWS account.</p>
</div></blockquote>
<p>Manages the account alias for the AWS Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account alias</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccountAlias.account_alias">
<code class="sig-name descname">account_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The account alias</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountAlias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_alias=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountAlias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account alias</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountAlias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountAlias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountPasswordPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AccountPasswordPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_users_to_change_password=None</em>, <em class="sig-param">hard_expiry=None</em>, <em class="sig-param">max_password_age=None</em>, <em class="sig-param">minimum_password_length=None</em>, <em class="sig-param">password_reuse_prevention=None</em>, <em class="sig-param">require_lowercase_characters=None</em>, <em class="sig-param">require_numbers=None</em>, <em class="sig-param">require_symbols=None</em>, <em class="sig-param">require_uppercase_characters=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.</p>
</div></blockquote>
<p>Manages Password Policy for the AWS Account.
See more about <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html">Account Password Policy</a>
in the official AWS docs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_users_to_change_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow users to change their own password</p></li>
<li><p><strong>hard_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)</p></li>
<li><p><strong>max_password_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days that an user password is valid.</p></li>
<li><p><strong>minimum_password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum length to require for user passwords.</p></li>
<li><p><strong>password_reuse_prevention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of previous passwords that users are prevented from reusing.</p></li>
<li><p><strong>require_lowercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require lowercase characters for user passwords.</p></li>
<li><p><strong>require_numbers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require numbers for user passwords.</p></li>
<li><p><strong>require_symbols</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require symbols for user passwords.</p></li>
<li><p><strong>require_uppercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require uppercase characters for user passwords.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.allow_users_to_change_password">
<code class="sig-name descname">allow_users_to_change_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.allow_users_to_change_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow users to change their own password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.expire_passwords">
<code class="sig-name descname">expire_passwords</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.expire_passwords" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether passwords in the account expire.
Returns <code class="docutils literal notranslate"><span class="pre">true</span></code> if <code class="docutils literal notranslate"><span class="pre">max_password_age</span></code> contains a value greater than <code class="docutils literal notranslate"><span class="pre">0</span></code>.
Returns <code class="docutils literal notranslate"><span class="pre">false</span></code> if it is <code class="docutils literal notranslate"><span class="pre">0</span></code> or <em>not present</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.hard_expiry">
<code class="sig-name descname">hard_expiry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.hard_expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.max_password_age">
<code class="sig-name descname">max_password_age</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.max_password_age" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days that an user password is valid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.minimum_password_length">
<code class="sig-name descname">minimum_password_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.minimum_password_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum length to require for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.password_reuse_prevention">
<code class="sig-name descname">password_reuse_prevention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.password_reuse_prevention" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of previous passwords that users are prevented from reusing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_lowercase_characters">
<code class="sig-name descname">require_lowercase_characters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_lowercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require lowercase characters for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_numbers">
<code class="sig-name descname">require_numbers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_numbers" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require numbers for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_symbols">
<code class="sig-name descname">require_symbols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_symbols" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require symbols for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_uppercase_characters">
<code class="sig-name descname">require_uppercase_characters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_uppercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require uppercase characters for user passwords.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_users_to_change_password=None</em>, <em class="sig-param">expire_passwords=None</em>, <em class="sig-param">hard_expiry=None</em>, <em class="sig-param">max_password_age=None</em>, <em class="sig-param">minimum_password_length=None</em>, <em class="sig-param">password_reuse_prevention=None</em>, <em class="sig-param">require_lowercase_characters=None</em>, <em class="sig-param">require_numbers=None</em>, <em class="sig-param">require_symbols=None</em>, <em class="sig-param">require_uppercase_characters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountPasswordPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_users_to_change_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow users to change their own password</p></li>
<li><p><strong>expire_passwords</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether passwords in the account expire.
Returns <code class="docutils literal notranslate"><span class="pre">true</span></code> if <code class="docutils literal notranslate"><span class="pre">max_password_age</span></code> contains a value greater than <code class="docutils literal notranslate"><span class="pre">0</span></code>.
Returns <code class="docutils literal notranslate"><span class="pre">false</span></code> if it is <code class="docutils literal notranslate"><span class="pre">0</span></code> or <em>not present</em>.</p></li>
<li><p><strong>hard_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)</p></li>
<li><p><strong>max_password_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days that an user password is valid.</p></li>
<li><p><strong>minimum_password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum length to require for user passwords.</p></li>
<li><p><strong>password_reuse_prevention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of previous passwords that users are prevented from reusing.</p></li>
<li><p><strong>require_lowercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require lowercase characters for user passwords.</p></li>
<li><p><strong>require_numbers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require numbers for user passwords.</p></li>
<li><p><strong>require_symbols</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require symbols for user passwords.</p></li>
<li><p><strong>require_uppercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require uppercase characters for user passwords.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountPasswordPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AwaitableGetAccountAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetAccountAliasResult</code><span class="sig-paren">(</span><em class="sig-param">account_alias=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetAccountAliasResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetInstanceProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetInstanceProfileResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetInstanceProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetPolicyDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetPolicyDocumentResult</code><span class="sig-paren">(</span><em class="sig-param">json=None</em>, <em class="sig-param">override_json=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">source_json=None</em>, <em class="sig-param">statements=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetPolicyDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetRoleResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">assume_role_policy=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_session_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetServerCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetServerCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">latest=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">path_prefix=None</em>, <em class="sig-param">upload_date=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetServerCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetAccountAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetAccountAliasResult</code><span class="sig-paren">(</span><em class="sig-param">account_alias=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAlias.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetAccountAliasResult.account_alias">
<code class="sig-name descname">account_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias associated with the AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetAccountAliasResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the iam user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the iam user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>List of objects containing group member information. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetInstanceProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetInstanceProfileResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceProfile.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The string representation of the date the instance profile
was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role arn associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role id associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetPolicyDocumentResult</code><span class="sig-paren">(</span><em class="sig-param">json=None</em>, <em class="sig-param">override_json=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">source_json=None</em>, <em class="sig-param">statements=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyDocument.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult.json">
<code class="sig-name descname">json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult.json" title="Permalink to this definition">¶</a></dt>
<dd><p>The above arguments serialized as a standard JSON policy document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetRoleResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">assume_role_policy=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_session_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRole.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.assume_role_policy">
<code class="sig-name descname">assume_role_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.assume_role_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document associated with the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation date of the role in RFC 3339 format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.max_session_duration">
<code class="sig-name descname">max_session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.max_session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum session duration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.permissions_boundary">
<code class="sig-name descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetServerCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetServerCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">latest=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">path_prefix=None</em>, <em class="sig-param">upload_date=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetServerCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerCertificate.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetServerCertificateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetServerCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which this user was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.permissions_boundary">
<code class="sig-name descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name associated to this User</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <cite>=,.&#64;-*.</cite>. Group names are not distinguished by case. For example, you cannot create groups named both “ADMINS” and “admins”.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the group.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Group.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. Group names are not distinguished by case. For example, you cannot create groups named both “ADMINS” and “admins”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <cite>=,.&#64;-*.</cite>. Group names are not distinguished by case. For example, you cannot create groups named both “ADMINS” and “admins”.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the group.</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [unique ID][1] assigned by AWS.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GroupMembership</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>WARNING:</strong> Multiple iam.GroupMembership resources with the same group name will produce inconsistent behavior!</p>
</div></blockquote>
<p>Provides a top level resource to manage IAM Group membership for IAM Users. For
more information on managing IAM Groups or IAM Users, see [IAM Groups][1] or
[IAM Users][2]</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">iam.GroupMembership</span></code> will conflict with itself if used more than once with the same group. To non-exclusively manage the users in a group, see the
[<code class="docutils literal notranslate"><span class="pre">iam.UserGroupMembership</span></code> resource][3].</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Group name to attach the list of <code class="docutils literal notranslate"><span class="pre">users</span></code> to</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify the Group Membership</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IAM User names to associate with the Group</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.group">
<code class="sig-name descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Group name to attach the list of <code class="docutils literal notranslate"><span class="pre">users</span></code> to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify the Group Membership</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IAM User names to associate with the Group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Group name to attach the list of <code class="docutils literal notranslate"><span class="pre">users</span></code> to</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify the Group Membership</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IAM User names to associate with the Group</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GroupPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy attached to a group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM group to attach to the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will
assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicy.group">
<code class="sig-name descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM group to attach to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. If omitted, this provider will
assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicy.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM group to attach to the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will
assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">GroupPolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM group</p>
<blockquote>
<div><p><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">iam.PolicyAttachment</span></code> resource and will permanently show a difference if both are defined.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group the policy should be applied to</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.group">
<code class="sig-name descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.policy_arn">
<code class="sig-name descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">policy_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupPolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group the policy should be applied to</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.InstanceProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">InstanceProfile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM instance profile.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The profile’s name. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the profile.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name to include in the profile.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to <code class="docutils literal notranslate"><span class="pre">Cannot</span> <span class="pre">exceed</span> <span class="pre">quota</span> <span class="pre">for</span> <span class="pre">InstanceSessionsPerInstanceProfile:</span> <span class="pre">1</span></code>, then you must contact AWS support and ask for a limit increase.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation timestamp of the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The profile’s name. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name to include in the profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to <code class="docutils literal notranslate"><span class="pre">Cannot</span> <span class="pre">exceed</span> <span class="pre">quota</span> <span class="pre">for</span> <span class="pre">InstanceSessionsPerInstanceProfile:</span> <span class="pre">1</span></code>, then you must contact AWS support and ask for a limit increase.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.InstanceProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS to the instance profile.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation timestamp of the instance profile.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The profile’s name. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the profile.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name to include in the profile.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to <code class="docutils literal notranslate"><span class="pre">Cannot</span> <span class="pre">exceed</span> <span class="pre">quota</span> <span class="pre">for</span> <span class="pre">InstanceSessionsPerInstanceProfile:</span> <span class="pre">1</span></code>, then you must contact AWS support and ask for a limit increase.</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [unique ID][1] assigned by AWS.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.InstanceProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.InstanceProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.OpenIdConnectProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">OpenIdConnectProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id_lists=None</em>, <em class="sig-param">thumbprint_lists=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM OpenID Connect provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that’s sent as the client_id parameter on OAuth requests.)</p></li>
<li><p><strong>thumbprint_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider’s server certificate(s).</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the identity provider. Corresponds to the <em>iss</em> claim.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.client_id_lists">
<code class="sig-name descname">client_id_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.client_id_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that’s sent as the client_id parameter on OAuth requests.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.thumbprint_lists">
<code class="sig-name descname">thumbprint_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.thumbprint_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider’s server certificate(s).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the identity provider. Corresponds to the <em>iss</em> claim.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">client_id_lists=None</em>, <em class="sig-param">thumbprint_lists=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OpenIdConnectProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this provider.</p></li>
<li><p><strong>client_id_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that’s sent as the client_id parameter on OAuth requests.)</p></li>
<li><p><strong>thumbprint_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider’s server certificate(s).</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the identity provider. Corresponds to the <em>iss</em> claim.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.OpenIdConnectProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the IAM policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the policy.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the policy.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS to this policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the IAM policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Path in which to create the policy.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.PolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">PolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)</p>
<p>!&gt; <strong>WARNING:</strong> The iam.PolicyAttachment resource creates <strong>exclusive</strong> attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single iam.PolicyAttachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other resources managed by this provider) will have that attached policy revoked by this resource. Consider <code class="docutils literal notranslate"><span class="pre">iam.RolePolicyAttachment</span></code>, <code class="docutils literal notranslate"><span class="pre">iam.UserPolicyAttachment</span></code>, or <code class="docutils literal notranslate"><span class="pre">iam.GroupPolicyAttachment</span></code> instead. These resources do not enforce exclusive attachment of an IAM policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">iam.GroupPolicyAttachment</span></code>, <code class="docutils literal notranslate"><span class="pre">iam.RolePolicyAttachment</span></code>, and <code class="docutils literal notranslate"><span class="pre">iam.UserPolicyAttachment</span></code> resources and will permanently show a difference if both are defined.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The group(s) the policy should be applied to</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attachment. This cannot be an empty string.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The role(s) the policy should be applied to</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The user(s) the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The group(s) the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the attachment. This cannot be an empty string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.policy_arn">
<code class="sig-name descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The role(s) the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The user(s) the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.PolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The group(s) the policy should be applied to</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attachment. This cannot be an empty string.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The role(s) the policy should be applied to</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The user(s) the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.PolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.PolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">assume_role_policy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">force_detach_policies=None</em>, <em class="sig-param">max_session_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM role.</p>
<blockquote>
<div><p><em>NOTE:</em> If policies are attached to the role via the <cite>``iam.PolicyAttachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html</a>&gt;`_ and you are modifying the role <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">path</span></code>, the <code class="docutils literal notranslate"><span class="pre">force_detach_policies</span></code> argument must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> and applied before attempting the operation otherwise you will encounter a <code class="docutils literal notranslate"><span class="pre">DeleteConflict</span></code> error. The <cite>``iam.RolePolicyAttachment`</cite> resource (recommended) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html</a>&gt;`_ does not have this requirement.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assume_role_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy that grants an entity permission to assume the role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</p></li>
<li><p><strong>force_detach_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies to force detaching any policies the role has before destroying it. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>max_session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The path to the role.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</p></li>
<li><p><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the role.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM role</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Role.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.assume_role_policy">
<code class="sig-name descname">assume_role_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.assume_role_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy that grants an entity permission to assume the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the IAM role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.force_detach_policies">
<code class="sig-name descname">force_detach_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.force_detach_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies to force detaching any policies the role has before destroying it. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.max_session_duration">
<code class="sig-name descname">max_session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.max_session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the role.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.permissions_boundary">
<code class="sig-name descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the IAM role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">assume_role_policy=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">force_detach_policies=None</em>, <em class="sig-param">max_session_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the role.</p></li>
<li><p><strong>assume_role_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy that grants an entity permission to assume the role.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the IAM role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</p></li>
<li><p><strong>force_detach_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies to force detaching any policies the role has before destroying it. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>max_session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The path to the role.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</p></li>
<li><p><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the role.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM role</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stable and unique string identifying the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">RolePolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM role policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role policy. If omitted, this provider will
assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role to attach to the policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role policy. If omitted, this provider will
assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicy.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicy.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role to attach to the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RolePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role policy. If omitted, this provider will
assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role to attach to the policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">RolePolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM role</p>
<blockquote>
<div><p><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">iam.PolicyAttachment</span></code> resource and will permanently show a difference if both are defined.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicyAttachment.policy_arn">
<code class="sig-name descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicyAttachment.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RolePolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SamlProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">SamlProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">saml_metadata_document=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM SAML provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the provider to create.</p></li>
<li><p><strong>saml_metadata_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An XML document generated by an identity provider that supports SAML 2.0.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the provider to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.saml_metadata_document">
<code class="sig-name descname">saml_metadata_document</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.saml_metadata_document" title="Permalink to this definition">¶</a></dt>
<dd><p>An XML document generated by an identity provider that supports SAML 2.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.valid_until">
<code class="sig-name descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date and time for the SAML provider in RFC1123 format, e.g. <code class="docutils literal notranslate"><span class="pre">Mon,</span> <span class="pre">02</span> <span class="pre">Jan</span> <span class="pre">2006</span> <span class="pre">15:04:05</span> <span class="pre">MST</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SamlProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">saml_metadata_document=None</em>, <em class="sig-param">valid_until=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this provider.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the provider to create.</p></li>
<li><p><strong>saml_metadata_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An XML document generated by an identity provider that supports SAML 2.0.</p></li>
<li><p><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration date and time for the SAML provider in RFC1123 format, e.g. <code class="docutils literal notranslate"><span class="pre">Mon,</span> <span class="pre">02</span> <span class="pre">Jan</span> <span class="pre">2006</span> <span class="pre">15:04:05</span> <span class="pre">MST</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SamlProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SamlProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServerCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">ServerCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM Server Certificate resource to upload Server Certificates.
Certs uploaded to IAM can easily work with other AWS services such as:</p>
<ul class="simple">
<li><p>AWS Elastic Beanstalk</p></li>
<li><p>Elastic Load Balancing</p></li>
<li><p>CloudFront</p></li>
<li><p>AWS OpsWorks</p></li>
</ul>
<p>For information about server certificates in IAM, see [Managing Server
Certificates][2] in AWS Documentation.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the server certificate.</p></li>
<li><p><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the public key certificate in
PEM-encoded format.</p></li>
<li><p><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Server Certificate. Do not include the
path in this value. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format <code class="docutils literal notranslate"><span class="pre">/cloudfront/your_path_here</span></code>.
See [IAM Identifiers][1] for more details on IAM Paths.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the private key in PEM-encoded format.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the server certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.certificate_body">
<code class="sig-name descname">certificate_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.certificate_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the public key certificate in
PEM-encoded format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.certificate_chain">
<code class="sig-name descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Server Certificate. Do not include the
path in this value. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format <code class="docutils literal notranslate"><span class="pre">/cloudfront/your_path_here</span></code>.
See [IAM Identifiers][1] for more details on IAM Paths.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the private key in PEM-encoded format.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServerCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">private_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the server certificate.</p></li>
<li><p><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the public key certificate in
PEM-encoded format.</p></li>
<li><p><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Server Certificate. Do not include the
path in this value. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format <code class="docutils literal notranslate"><span class="pre">/cloudfront/your_path_here</span></code>.
See [IAM Identifiers][1] for more details on IAM Paths.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the private key in PEM-encoded format.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServerCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServerCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServiceLinkedRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">ServiceLinkedRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_service_name=None</em>, <em class="sig-param">custom_suffix=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html">IAM service-linked role</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS service to which this role is attached. You use a string similar to a URL but without the <code class="docutils literal notranslate"><span class="pre">http://</span></code> in front. For example: <code class="docutils literal notranslate"><span class="pre">elasticbeanstalk.amazonaws.com</span></code>. To find the full list of services that support service-linked roles, check <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">the docs</a>.</p></li>
<li><p><strong>custom_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional string appended to the role name. Not all AWS services support custom suffixes.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.aws_service_name">
<code class="sig-name descname">aws_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.aws_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service to which this role is attached. You use a string similar to a URL but without the <code class="docutils literal notranslate"><span class="pre">http://</span></code> in front. For example: <code class="docutils literal notranslate"><span class="pre">elasticbeanstalk.amazonaws.com</span></code>. To find the full list of services that support service-linked roles, check <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">the docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the IAM role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.custom_suffix">
<code class="sig-name descname">custom_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.custom_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional string appended to the role name. Not all AWS services support custom suffixes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServiceLinkedRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_service_name=None</em>, <em class="sig-param">create_date=None</em>, <em class="sig-param">custom_suffix=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceLinkedRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the role.</p></li>
<li><p><strong>aws_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service to which this role is attached. You use a string similar to a URL but without the <code class="docutils literal notranslate"><span class="pre">http://</span></code> in front. For example: <code class="docutils literal notranslate"><span class="pre">elasticbeanstalk.amazonaws.com</span></code>. To find the full list of services that support service-linked roles, check <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">the docs</a>.</p>
</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the IAM role.</p></li>
<li><p><strong>custom_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional string appended to the role name. Not all AWS services support custom suffixes.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the role.</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stable and unique string identifying the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServiceLinkedRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServiceLinkedRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Uploads an SSH public key and associates it with the specified IAM user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code class="docutils literal notranslate"><span class="pre">SSH</span></code>. To retrieve the public key in PEM format, use <code class="docutils literal notranslate"><span class="pre">PEM</span></code>.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is <code class="docutils literal notranslate"><span class="pre">active</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM user to associate the SSH public key with.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.encoding">
<code class="sig-name descname">encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code class="docutils literal notranslate"><span class="pre">SSH</span></code>. To retrieve the public key in PEM format, use <code class="docutils literal notranslate"><span class="pre">PEM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 message digest of the SSH public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.ssh_public_key_id">
<code class="sig-name descname">ssh_public_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.ssh_public_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the SSH public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is <code class="docutils literal notranslate"><span class="pre">active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM user to associate the SSH public key with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">ssh_public_key_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code class="docutils literal notranslate"><span class="pre">SSH</span></code>. To retrieve the public key in PEM format, use <code class="docutils literal notranslate"><span class="pre">PEM</span></code>.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MD5 message digest of the SSH public key.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.</p></li>
<li><p><strong>ssh_public_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the SSH public key.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is <code class="docutils literal notranslate"><span class="pre">active</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM user to associate the SSH public key with.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM user.</p>
<blockquote>
<div><p><em>NOTE:</em> If policies are attached to the user via the <cite>``iam.PolicyAttachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html</a>&gt;`_ and you are modifying the user <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">path</span></code>, the <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> argument must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> and applied before attempting the operation otherwise you will encounter a <code class="docutils literal notranslate"><span class="pre">DeleteConflict</span></code> error. The <cite>``iam.UserPolicyAttachment`</cite> resource (recommended) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_user_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_user_policy_attachment.html</a>&gt;`_ does not have this requirement.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When destroying this user, destroy even if it
has non-this provider-managed IAM access keys, login profile or MFA devices. Without <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code>
a user with non-this provider-managed access keys and login profile will fail to be destroyed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. User names are not distinguished by case. For example, you cannot create users named both “TESTUSER” and “testuser”.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the user.</p></li>
<li><p><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the user.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM user</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.User.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>When destroying this user, destroy even if it
has non-this provider-managed IAM access keys, login profile or MFA devices. Without <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code>
a user with non-this provider-managed access keys and login profile will fail to be destroyed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. User names are not distinguished by case. For example, you cannot create users named both “TESTUSER” and “testuser”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.permissions_boundary">
<code class="sig-name descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the IAM user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">permissions_boundary=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this user.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When destroying this user, destroy even if it
has non-this provider-managed IAM access keys, login profile or MFA devices. Without <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code>
a user with non-this provider-managed access keys and login profile will fail to be destroyed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. User names are not distinguished by case. For example, you cannot create users named both “TESTUSER” and “testuser”.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the user.</p></li>
<li><p><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the user.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM user</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [unique ID][1] assigned by AWS.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserGroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">UserGroupMembership</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.</p>
<p>To exclusively manage the users in a group, see the
[<code class="docutils literal notranslate"><span class="pre">iam.GroupMembership</span></code> resource][3].</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of [IAM Groups][1] to add the user to</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the [IAM User][2] to add to groups</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserGroupMembership.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of [IAM Groups][1] to add the user to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserGroupMembership.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the [IAM User][2] to add to groups</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserGroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserGroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of [IAM Groups][1] to add the user to</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the [IAM User][2] to add to groups</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserGroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserGroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserLoginProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">UserLoginProfile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">password_length=None</em>, <em class="sig-param">password_reset_required=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IAM User Login Profile with limited support for password creation during this provider resource creation. Uses PGP to encrypt the password for safe transport to the user. PGP keys can be obtained from Keybase.</p>
<blockquote>
<div><p>To reset an IAM User login password via this provider, you can use delete and recreate this resource or change any of the arguments.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>password_reset_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:username</span></code>. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user’s name.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.encrypted_password">
<code class="sig-name descname">encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.key_fingerprint">
<code class="sig-name descname">key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.password_length">
<code class="sig-name descname">password_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.password_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.password_reset_required">
<code class="sig-name descname">password_reset_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.password_reset_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.pgp_key">
<code class="sig-name descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:username</span></code>. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user’s name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserLoginProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encrypted_password=None</em>, <em class="sig-param">key_fingerprint=None</em>, <em class="sig-param">password_length=None</em>, <em class="sig-param">password_reset_required=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserLoginProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.</p></li>
<li><p><strong>key_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.</p></li>
<li><p><strong>password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>password_reset_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:username</span></code>. Only applies on resource creation. Drift detection is not possible with this argument.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user’s name.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserLoginProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserLoginProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">UserPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy attached to a user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM user to which to attach this policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicy.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicy.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.user" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM user to which to attach this policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM user to which to attach this policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">UserPolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM user</p>
<blockquote>
<div><p><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">iam.PolicyAttachment</span></code> resource and will permanently show a difference if both are defined.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicyAttachment.policy_arn">
<code class="sig-name descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicyAttachment.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_arn=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user the policy should be applied to</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.get_account_alias">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_account_alias</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Account Alias data source allows access to the account alias
for the effective account in which this provider is working.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_account_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_account_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_group">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM group. By using this data source, you can reference IAM group
properties without having to hard code ARNs as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>group_name</strong> (<em>str</em>) – The friendly IAM group name to match.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_instance_profile">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_instance_profile</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM instance profile. By using this data source, you can reference IAM
instance profile properties without having to hard code ARNs as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The friendly IAM instance profile name to match.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_instance_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_instance_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_policy">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_policy</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>arn</strong> (<em>str</em>) – ARN of the IAM policy.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_policy_document">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_policy_document</code><span class="sig-paren">(</span><em class="sig-param">override_json=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">source_json=None</em>, <em class="sig-param">statements=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>override_json</strong> (<em>str</em>) – An IAM policy document to import and override the
current policy document.  Statements with non-blank <code class="docutils literal notranslate"><span class="pre">sid</span></code>s in the override
document will overwrite statements with the same <code class="docutils literal notranslate"><span class="pre">sid</span></code> in the current document.
Statements without an <code class="docutils literal notranslate"><span class="pre">sid</span></code> cannot be overwritten.</p></li>
<li><p><strong>policy_id</strong> (<em>str</em>) – An ID for the policy document.</p></li>
<li><p><strong>source_json</strong> (<em>str</em>) – An IAM policy document to import as a base for the
current policy document.  Statements with non-blank <code class="docutils literal notranslate"><span class="pre">sid</span></code>s in the current
policy document will overwrite statements with the same <code class="docutils literal notranslate"><span class="pre">sid</span></code> in the source
json.  Statements without an <code class="docutils literal notranslate"><span class="pre">sid</span></code> cannot be overwritten.</p></li>
<li><p><strong>statements</strong> (<em>list</em>) – A nested configuration block (described below)
configuring one <em>statement</em> to be included in the policy document.</p></li>
<li><p><strong>version</strong> (<em>str</em>) – IAM policy document version. Valid values: <code class="docutils literal notranslate"><span class="pre">2008-10-17</span></code>, <code class="docutils literal notranslate"><span class="pre">2012-10-17</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">2012-10-17</span></code>. For more information, see the <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html">AWS IAM User Guide</a>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of actions that this statement either allows
or denies. For example, <code class="docutils literal notranslate"><span class="pre">[&quot;ec2:RunInstances&quot;,</span> <span class="pre">&quot;s3:*&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">test</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the
<a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html">IAM condition operator</a>
to evaluate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the “OR” boolean operation.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a
<a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys">Context Variable</a>
to apply the condition to. Context variables may either be standard AWS
variables starting with <code class="docutils literal notranslate"><span class="pre">aws:</span></code>, or service-specific variables prefixed with
the service name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Either “Allow” or “Deny”, to specify whether this
statement allows or denies the given actions. The default is “Allow”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of actions that this statement does <em>not</em>
apply to. Used to apply a policy statement to all actions <em>except</em> those
listed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notPrincipals</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Like <code class="docutils literal notranslate"><span class="pre">principals</span></code> except gives resources that
the statement does <em>not</em> apply to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identifiers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of identifiers for principals. When <code class="docutils literal notranslate"><span class="pre">type</span></code>
is “AWS”, these are IAM user or role ARNs.  When <code class="docutils literal notranslate"><span class="pre">type</span></code> is “Service”, these are AWS Service roles e.g. <code class="docutils literal notranslate"><span class="pre">lambda.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of principal. For AWS ARNs this is “AWS”.  For AWS services (e.g. Lambda), this is “Service”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">notResources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of resource ARNs that this statement
does <em>not</em> apply to. Used to apply a policy statement to all resources
<em>except</em> those listed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principals</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identifiers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of identifiers for principals. When <code class="docutils literal notranslate"><span class="pre">type</span></code>
is “AWS”, these are IAM user or role ARNs.  When <code class="docutils literal notranslate"><span class="pre">type</span></code> is “Service”, these are AWS Service roles e.g. <code class="docutils literal notranslate"><span class="pre">lambda.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of principal. For AWS ARNs this is “AWS”.  For AWS services (e.g. Lambda), this is “Service”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An ID for the policy statement.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy_document.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy_document.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_role">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_role</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM role. By using this data source, you can reference IAM role
properties without having to hard code ARNs as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The friendly IAM role name to match.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_server_certificate">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_server_certificate</code><span class="sig-paren">(</span><em class="sig-param">latest=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">path_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_server_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to lookup information about IAM Server Certificates.</p>
<p>The import function will read in certificate body, certificate chain (if it exists), id, name, path, and arn. 
It will not retrieve the private key which is not available through the AWS API.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>latest</strong> (<em>bool</em>) – sort results by expiration date. returns the certificate with expiration date in furthest in the future.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – exact name of the cert to lookup</p></li>
<li><p><strong>name_prefix</strong> (<em>str</em>) – prefix of cert to filter by</p></li>
<li><p><strong>path_prefix</strong> (<em>str</em>) – prefix of path to filter by</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_user">
<code class="sig-prename descclassname">pulumi_aws.iam.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">user_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM user. By using this data source, you can reference IAM user
properties without having to hard code ARNs or unique IDs as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>user_name</strong> (<em>str</em>) – The friendly IAM user name to match.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_user.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
