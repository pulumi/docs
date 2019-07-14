---
---

<div class="section" id="iam">
<h1>iam<a class="headerlink" href="#iam" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.iam"></span><dl class="class">
<dt id="pulumi_aws.iam.AccessKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">AccessKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>pgp_key=None</em>, <em>status=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a
keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</li>
<li><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key status to apply. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> and <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user to associate with this access key.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_access_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.key_fingerprint">
<code class="descname">key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt
the secret</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.pgp_key">
<code class="descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a
keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.secret">
<code class="descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret access key. Note that this will be written
to the state file. Please supply a <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> instead, which will prevent the
secret from being stored in plain text</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.ses_smtp_password">
<code class="descname">ses_smtp_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.ses_smtp_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret access key converted into an SES SMTP
password by applying <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credentials-convert">AWS’s documented conversion
algorithm</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The access key status to apply. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> and <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccessKey.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccessKey.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user to associate with this access key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccessKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccessKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccessKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountAlias">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">AccountAlias</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_alias=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Note:</strong> There is only a single account alias per AWS account.</div></blockquote>
<p>Manages the account alias for the AWS Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account alias</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccountAlias.account_alias">
<code class="descname">account_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The account alias</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountAlias.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountAlias.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountPasswordPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">AccountPasswordPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_users_to_change_password=None</em>, <em>hard_expiry=None</em>, <em>max_password_age=None</em>, <em>minimum_password_length=None</em>, <em>password_reuse_prevention=None</em>, <em>require_lowercase_characters=None</em>, <em>require_numbers=None</em>, <em>require_symbols=None</em>, <em>require_uppercase_characters=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Note:</strong> There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.</div></blockquote>
<p>Manages Password Policy for the AWS Account.
See more about <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html">Account Password Policy</a>
in the official AWS docs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_users_to_change_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow users to change their own password</li>
<li><strong>hard_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)</li>
<li><strong>max_password_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days that an user password is valid.</li>
<li><strong>minimum_password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum length to require for user passwords.</li>
<li><strong>password_reuse_prevention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of previous passwords that users are prevented from reusing.</li>
<li><strong>require_lowercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require lowercase characters for user passwords.</li>
<li><strong>require_numbers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require numbers for user passwords.</li>
<li><strong>require_symbols</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require symbols for user passwords.</li>
<li><strong>require_uppercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to require uppercase characters for user passwords.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.allow_users_to_change_password">
<code class="descname">allow_users_to_change_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.allow_users_to_change_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow users to change their own password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.expire_passwords">
<code class="descname">expire_passwords</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.expire_passwords" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether passwords in the account expire.
Returns <code class="docutils literal notranslate"><span class="pre">true</span></code> if <code class="docutils literal notranslate"><span class="pre">max_password_age</span></code> contains a value greater than <code class="docutils literal notranslate"><span class="pre">0</span></code>.
Returns <code class="docutils literal notranslate"><span class="pre">false</span></code> if it is <code class="docutils literal notranslate"><span class="pre">0</span></code> or <em>not present</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.hard_expiry">
<code class="descname">hard_expiry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.hard_expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.max_password_age">
<code class="descname">max_password_age</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.max_password_age" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days that an user password is valid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.minimum_password_length">
<code class="descname">minimum_password_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.minimum_password_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum length to require for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.password_reuse_prevention">
<code class="descname">password_reuse_prevention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.password_reuse_prevention" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of previous passwords that users are prevented from reusing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_lowercase_characters">
<code class="descname">require_lowercase_characters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_lowercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require lowercase characters for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_numbers">
<code class="descname">require_numbers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_numbers" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require numbers for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_symbols">
<code class="descname">require_symbols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_symbols" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require symbols for user passwords.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.require_uppercase_characters">
<code class="descname">require_uppercase_characters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.require_uppercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to require uppercase characters for user passwords.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.AccountPasswordPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.AccountPasswordPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.AccountPasswordPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GetAccountAliasResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetAccountAliasResult</code><span class="sig-paren">(</span><em>account_alias=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAlias.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetAccountAliasResult.account_alias">
<code class="descname">account_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias associated with the AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetAccountAliasResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetAccountAliasResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>group_id=None</em>, <em>group_name=None</em>, <em>path=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.group_id">
<code class="descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetInstanceProfileResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetInstanceProfileResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>create_date=None</em>, <em>name=None</em>, <em>path=None</em>, <em>role_arn=None</em>, <em>role_id=None</em>, <em>role_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceProfile.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.create_date">
<code class="descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The string representation of the date the instance profile
was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role arn associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_id">
<code class="descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role id associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.role_name">
<code class="descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name associated with this instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetInstanceProfileResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetInstanceProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetPolicyDocumentResult</code><span class="sig-paren">(</span><em>json=None</em>, <em>override_json=None</em>, <em>policy_id=None</em>, <em>source_json=None</em>, <em>statements=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyDocument.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult.json">
<code class="descname">json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult.json" title="Permalink to this definition">¶</a></dt>
<dd><p>The above arguments serialized as a standard JSON policy document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyDocumentResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyDocumentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetPolicyResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>description=None</em>, <em>name=None</em>, <em>path=None</em>, <em>policy=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetRoleResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetRoleResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>assume_role_policy=None</em>, <em>create_date=None</em>, <em>description=None</em>, <em>max_session_duration=None</em>, <em>name=None</em>, <em>path=None</em>, <em>permissions_boundary=None</em>, <em>unique_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRole.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.assume_role_policy">
<code class="descname">assume_role_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.assume_role_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document associated with the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.create_date">
<code class="descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation date of the role in RFC 3339 format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.max_session_duration">
<code class="descname">max_session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.max_session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum session duration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.permissions_boundary">
<code class="descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetRoleResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetServerCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetServerCertificateResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>expiration_date=None</em>, <em>latest=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path=None</em>, <em>path_prefix=None</em>, <em>upload_date=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetServerCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerCertificate.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetServerCertificateResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetServerCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>path=None</em>, <em>permissions_boundary=None</em>, <em>user_id=None</em>, <em>user_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which this user was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.permissions_boundary">
<code class="descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.user_name">
<code class="descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name associated to this User</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GetUserResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iam.Group">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>path=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <cite>=,.&#64;-*.</cite>. Group names are not distinguished by case. For example, you cannot create groups named both “ADMINS” and “admins”.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Group.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. Group names are not distinguished by case. For example, you cannot create groups named both “ADMINS” and “admins”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Group.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Group.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupMembership">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GroupMembership</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>group=None</em>, <em>name=None</em>, <em>users=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>WARNING:</strong> Multiple aws_iam_group_membership resources with the same group name will produce inconsistent behavior!</div></blockquote>
<p>Provides a top level resource to manage IAM Group membership for IAM Users. For
more information on managing IAM Groups or IAM Users, see [IAM Groups][1] or
[IAM Users][2]</p>
<blockquote>
<div><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">aws_iam_group_membership</span></code> will conflict with itself if used more than once with the same group. To non-exclusively manage the users in a group, see the
[<code class="docutils literal notranslate"><span class="pre">aws_iam_user_group_membership</span></code> resource][3].</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Group name to attach the list of <code class="docutils literal notranslate"><span class="pre">users</span></code> to</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify the Group Membership</li>
<li><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IAM User names to associate with the Group</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_membership.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.group">
<code class="descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Group name to attach the list of <code class="docutils literal notranslate"><span class="pre">users</span></code> to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify the Group Membership</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupMembership.users">
<code class="descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IAM User names to associate with the Group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupMembership.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupMembership.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GroupPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>group=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy attached to a group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM group to attach to the policy.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicy.group">
<code class="descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM group to attach to the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicy.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">GroupPolicyAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>group=None</em>, <em>policy_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM group</p>
<blockquote>
<div><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">aws_iam_policy_attachment</span></code> resource and will permanently show a difference if both are defined.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group the policy should be applied to</li>
<li><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_group_policy_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.group">
<code class="descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.policy_arn">
<code class="descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.GroupPolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.GroupPolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.GroupPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.InstanceProfile">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">InstanceProfile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path=None</em>, <em>role=None</em>, <em>roles=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM instance profile.</p>
<blockquote>
<div><strong>NOTE:</strong> Either <code class="docutils literal notranslate"><span class="pre">role</span></code> or <code class="docutils literal notranslate"><span class="pre">roles</span></code> (<strong>deprecated</strong>) must be specified.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the profile.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name to include in the profile.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.create_date">
<code class="descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation timestamp of the instance profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name to include in the profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.InstanceProfile.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.InstanceProfile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.InstanceProfile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.InstanceProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.OpenIdConnectProvider">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">OpenIdConnectProvider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>client_id_lists=None</em>, <em>thumbprint_lists=None</em>, <em>url=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM OpenID Connect provider.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>client_id_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that’s sent as the client_id parameter on OAuth requests.)</li>
<li><strong>thumbprint_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider’s server certificate(s).</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the identity provider. Corresponds to the <em>iss</em> claim.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.client_id_lists">
<code class="descname">client_id_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.client_id_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that’s sent as the client_id parameter on OAuth requests.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.thumbprint_lists">
<code class="descname">thumbprint_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.thumbprint_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider’s server certificate(s).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the identity provider. Corresponds to the <em>iss</em> claim.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.OpenIdConnectProvider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.OpenIdConnectProvider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.OpenIdConnectProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Policy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the IAM policy.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the policy.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Policy.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Policy.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the policy.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.PolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">PolicyAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>groups=None</em>, <em>name=None</em>, <em>policy_arn=None</em>, <em>roles=None</em>, <em>users=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PolicyAttachment resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The group(s) the policy should be applied to</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attachment. This cannot be an empty string.</li>
<li><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The role(s) the policy should be applied to</li>
<li><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The user(s) the policy should be applied to</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_policy_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.groups">
<code class="descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The group(s) the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the attachment. This cannot be an empty string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.policy_arn">
<code class="descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The role(s) the policy should be applied to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.PolicyAttachment.users">
<code class="descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The user(s) the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.PolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.PolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Role">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">Role</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>assume_role_policy=None</em>, <em>description=None</em>, <em>force_detach_policies=None</em>, <em>max_session_duration=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path=None</em>, <em>permissions_boundary=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM role.</p>
<blockquote>
<div><em>NOTE:</em> If policies are attached to the role via the <cite>``aws_iam_policy_attachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html</a>&gt;`_ and you are modifying the role <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">path</span></code>, the <code class="docutils literal notranslate"><span class="pre">force_detach_policies</span></code> argument must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> and applied before attempting the operation otherwise you will encounter a <code class="docutils literal notranslate"><span class="pre">DeleteConflict</span></code> error. The <cite>``aws_iam_role_policy_attachment`</cite> resource (recommended) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html</a>&gt;`_ does not have this requirement.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>assume_role_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy that grants an entity permission to assume the role.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</li>
<li><strong>force_detach_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies to force detaching any policies the role has before destroying it. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>max_session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The path to the role.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</li>
<li><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the role.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM role</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.Role.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.assume_role_policy">
<code class="descname">assume_role_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.assume_role_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy that grants an entity permission to assume the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.create_date">
<code class="descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the IAM role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.force_detach_policies">
<code class="descname">force_detach_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.force_detach_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies to force detaching any policies the role has before destroying it. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.max_session_duration">
<code class="descname">max_session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.max_session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the role.
See <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.permissions_boundary">
<code class="descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the IAM role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.Role.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.Role.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.Role.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.Role.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">RolePolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM role policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role to attach to the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicy.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicy.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role to attach to the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">RolePolicyAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_arn=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM role</p>
<blockquote>
<div><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">aws_iam_policy_attachment</span></code> resource and will permanently show a difference if both are defined.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role the policy should be applied to</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicyAttachment.policy_arn">
<code class="descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.RolePolicyAttachment.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.RolePolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.RolePolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.RolePolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SamlProvider">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">SamlProvider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>saml_metadata_document=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM SAML provider.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the provider to create.</li>
<li><strong>saml_metadata_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An XML document generated by an identity provider that supports SAML 2.0.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_saml_provider.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the provider to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.saml_metadata_document">
<code class="descname">saml_metadata_document</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.saml_metadata_document" title="Permalink to this definition">¶</a></dt>
<dd><p>An XML document generated by an identity provider that supports SAML 2.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SamlProvider.valid_until">
<code class="descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date and time for the SAML provider in RFC1123 format, e.g. <code class="docutils literal notranslate"><span class="pre">Mon,</span> <span class="pre">02</span> <span class="pre">Jan</span> <span class="pre">2006</span> <span class="pre">15:04:05</span> <span class="pre">MST</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SamlProvider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SamlProvider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SamlProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServerCertificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">ServerCertificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>arn=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path=None</em>, <em>private_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM Server Certificate resource to upload Server Certificates.
Certs uploaded to IAM can easily work with other AWS services such as:</p>
<ul class="simple">
<li>AWS Elastic Beanstalk</li>
<li>Elastic Load Balancing</li>
<li>CloudFront</li>
<li>AWS OpsWorks</li>
</ul>
<p>For information about server certificates in IAM, see [Managing Server
Certificates][2] in AWS Documentation.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the server certificate.</li>
<li><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the public key certificate in
PEM-encoded format.</li>
<li><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format <code class="docutils literal notranslate"><span class="pre">/cloudfront/your_path_here</span></code>.
See [IAM Identifiers][1] for more details on IAM Paths.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the private key in PEM-encoded format.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the server certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.certificate_body">
<code class="descname">certificate_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.certificate_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the public key certificate in
PEM-encoded format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the certificate chain.
This is typically a concatenation of the PEM-encoded public key certificates
of the chain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM path for the server certificate.  If it is not
included, it defaults to a slash (/). If this certificate is for use with
AWS CloudFront, the path must be in format <code class="docutils literal notranslate"><span class="pre">/cloudfront/your_path_here</span></code>.
See [IAM Identifiers][1] for more details on IAM Paths.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServerCertificate.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the private key in PEM-encoded format.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServerCertificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServerCertificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServerCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServiceLinkedRole">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">ServiceLinkedRole</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aws_service_name=None</em>, <em>custom_suffix=None</em>, <em>description=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html">IAM service-linked role</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aws_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS service to which this role is attached. You use a string similar to a URL but without the <code class="docutils literal notranslate"><span class="pre">http://</span></code> in front. For example: <code class="docutils literal notranslate"><span class="pre">elasticbeanstalk.amazonaws.com</span></code>. To find the full list of services that support service-linked roles, check <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">the docs</a>.</li>
<li><strong>custom_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional string appended to the role name. Not all AWS services support custom suffixes.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.aws_service_name">
<code class="descname">aws_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.aws_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service to which this role is attached. You use a string similar to a URL but without the <code class="docutils literal notranslate"><span class="pre">http://</span></code> in front. For example: <code class="docutils literal notranslate"><span class="pre">elasticbeanstalk.amazonaws.com</span></code>. To find the full list of services that support service-linked roles, check <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">the docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.create_date">
<code class="descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the IAM role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.custom_suffix">
<code class="descname">custom_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.custom_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional string appended to the role name. Not all AWS services support custom suffixes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.ServiceLinkedRole.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable and unique string identifying the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.ServiceLinkedRole.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.ServiceLinkedRole.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.ServiceLinkedRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SshKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">SshKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>encoding=None</em>, <em>public_key=None</em>, <em>status=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Uploads an SSH public key and associates it with the specified IAM user.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code class="docutils literal notranslate"><span class="pre">SSH</span></code>. To retrieve the public key in PEM format, use <code class="docutils literal notranslate"><span class="pre">PEM</span></code>.</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.</li>
<li><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is <code class="docutils literal notranslate"><span class="pre">active</span></code>.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IAM user to associate the SSH public key with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_ssh_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.encoding">
<code class="descname">encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code class="docutils literal notranslate"><span class="pre">SSH</span></code>. To retrieve the public key in PEM format, use <code class="docutils literal notranslate"><span class="pre">PEM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 message digest of the SSH public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.ssh_public_key_id">
<code class="descname">ssh_public_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.ssh_public_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the SSH public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is <code class="docutils literal notranslate"><span class="pre">active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.SshKey.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.SshKey.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IAM user to associate the SSH public key with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.SshKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.SshKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.User">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>force_destroy=None</em>, <em>name=None</em>, <em>path=None</em>, <em>permissions_boundary=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM user.</p>
<blockquote>
<div><em>NOTE:</em> If policies are attached to the user via the <cite>``aws_iam_policy_attachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html</a>&gt;`_ and you are modifying the user <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">path</span></code>, the <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> argument must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> and applied before attempting the operation otherwise you will encounter a <code class="docutils literal notranslate"><span class="pre">DeleteConflict</span></code> error. The <cite>``aws_iam_user_policy_attachment`</cite> resource (recommended) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_user_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_user_policy_attachment.html</a>&gt;`_ does not have this requirement.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <cite>=,.&#64;-*.</cite>. User names are not distinguished by case. For example, you cannot create users named both “TESTUSER” and “testuser”.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path in which to create the user.</li>
<li><strong>permissions_boundary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy that is used to set the permissions boundary for the user.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the IAM user</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.User.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: <code class="docutils literal notranslate"><span class="pre">=,.&#64;-_.</span></code>. User names are not distinguished by case. For example, you cannot create users named both “TESTUSER” and “testuser”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path in which to create the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.permissions_boundary">
<code class="descname">permissions_boundary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.permissions_boundary" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy that is used to set the permissions boundary for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the IAM user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.User.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.User.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The [unique ID][1] assigned by AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserGroupMembership">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">UserGroupMembership</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>groups=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.</p>
<p>To exclusively manage the users in a group, see the
[<code class="docutils literal notranslate"><span class="pre">aws_iam_group_membership</span></code> resource][3].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of [IAM Groups][1] to add the user to</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the [IAM User][2] to add to groups</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_group_membership.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserGroupMembership.groups">
<code class="descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of [IAM Groups][1] to add the user to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserGroupMembership.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the [IAM User][2] to add to groups</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserGroupMembership.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserGroupMembership.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserGroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserLoginProfile">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">UserLoginProfile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>password_length=None</em>, <em>password_reset_required=None</em>, <em>pgp_key=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UserLoginProfile resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</li>
<li><strong>password_reset_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</li>
<li><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:username</span></code>. Only applies on resource creation. Drift detection is not possible with this argument.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user’s name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.password_length">
<code class="descname">password_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.password_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.password_reset_required">
<code class="descname">password_reset_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.password_reset_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.pgp_key">
<code class="descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:username</span></code>. Only applies on resource creation. Drift detection is not possible with this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserLoginProfile.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user’s name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserLoginProfile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserLoginProfile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserLoginProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">UserPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IAM policy attached to a user.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM user to which to attach this policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicy.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicy.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.user" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM user to which to attach this policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iam.</code><code class="descname">UserPolicyAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_arn=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Managed IAM Policy to an IAM user</p>
<blockquote>
<div><strong>NOTE:</strong> The usage of this resource conflicts with the <code class="docutils literal notranslate"><span class="pre">aws_iam_policy_attachment</span></code> resource and will permanently show a difference if both are defined.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the policy you want to apply</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user the policy should be applied to</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicyAttachment.policy_arn">
<code class="descname">policy_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.policy_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the policy you want to apply</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iam.UserPolicyAttachment.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user the policy should be applied to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iam.UserPolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.UserPolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.UserPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iam.get_account_alias">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_account_alias</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_account_alias" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_account_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_account_alias.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_group">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM group. By using this data source, you can reference IAM group
properties without having to hard code ARNs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_instance_profile">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_instance_profile</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM instance profile. By using this data source, you can reference IAM
instance profile properties without having to hard code ARNs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_instance_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_instance_profile.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_policy">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_policy</code><span class="sig-paren">(</span><em>arn=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM policy.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_policy_document">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_policy_document</code><span class="sig-paren">(</span><em>override_json=None</em>, <em>policy_id=None</em>, <em>source_json=None</em>, <em>statements=None</em>, <em>version=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_policy_document" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy_document.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy_document.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_role">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_role</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM role. By using this data source, you can reference IAM role
properties without having to hard code ARNs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_role.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_server_certificate">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_server_certificate</code><span class="sig-paren">(</span><em>latest=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>path_prefix=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_server_certificate" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.iam.get_user">
<code class="descclassname">pulumi_aws.iam.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>user_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iam.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch information about a specific
IAM user. By using this data source, you can reference IAM user
properties without having to hard code ARNs or unique IDs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_user.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_user.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
