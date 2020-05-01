---
title: Module ram
title_tag: Module ram | Package pulumi_alicloud | Python SDK
linktitle: ram
notitle: true
---

<div class="section" id="ram">
<h1>ram<a class="headerlink" href="#ram" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.ram"></span><dl class="py class">
<dt id="pulumi_alicloud.ram.AccessKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AccessKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM User access key resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  You should set the <code class="docutils literal notranslate"><span class="pre">secret_file</span></code> if you want to get the access key.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code></p></li>
<li><p><strong>secret_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of file that can save access key id and access key secret. Strongly suggest you to specified it when you creating access key, otherwise, you wouldn’t get its secret ever.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of access key. It must be <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id3"><span class="problematic" id="id4">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccessKey.key_fingerprint">
<code class="sig-name descname">key_fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt the secret</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccessKey.pgp_key">
<code class="sig-name descname">pgp_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccessKey.secret_file">
<code class="sig-name descname">secret_file</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.secret_file" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of file that can save access key id and access key secret. Strongly suggest you to specified it when you creating access key, otherwise, you wouldn’t get its secret ever.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccessKey.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of access key. It must be <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccessKey.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccessKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the PGP key used to encrypt the secret</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code></p></li>
<li><p><strong>secret_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of file that can save access key id and access key secret. Strongly suggest you to specified it when you creating access key, otherwise, you wouldn’t get its secret ever.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of access key. It must be <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Inactive</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id7"><span class="problematic" id="id8">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccessKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccessKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccessKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.AccountAlias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AccountAlias</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountAlias" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM cloud account alias.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as “-“, and must not begin with a hyphen.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountAlias.account_alias">
<code class="sig-name descname">account_alias</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountAlias.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountAlias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountAlias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountAlias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as “-“, and must not begin with a hyphen.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountAlias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountAlias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AccountPasswordPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hard_expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_login_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_password_age</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_password_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reuse_prevention</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_lowercase_characters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_numbers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_symbols</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_uppercase_characters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AccountPasswordPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] hard_expiry: Specifies if a password can expire in a hard way. Default to false.
:param pulumi.Input[float] max_login_attempts: Maximum logon attempts with an incorrect password within an hour. Valid value range: [0-32]. Default to 5.
:param pulumi.Input[float] max_password_age: The number of days after which password expires. A value of 0 indicates that the password never expires. Valid value range: [0-1095]. Default to 0.
:param pulumi.Input[float] minimum_password_length: Minimal required length of password for a user. Valid value range: [8-32]. Default to 12.
:param pulumi.Input[float] password_reuse_prevention: User is not allowed to use the latest number of passwords specified in this parameter. A value of 0 indicates the password history check policy is disabled. Valid value range: [0-24]. Default to 0.
:param pulumi.Input[bool] require_lowercase_characters: Specifies if the occurrence of a lowercase character in the password is mandatory. Default to true.
:param pulumi.Input[bool] require_numbers: Specifies if the occurrence of a number in the password is mandatory. Default to true.
:param pulumi.Input[bool] require_symbols: (Optional Specifies if the occurrence of a special character in the password is mandatory. Default to true.
:param pulumi.Input[bool] require_uppercase_characters: Specifies if the occurrence of an uppercase character in the password is mandatory. Default to true.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.hard_expiry">
<code class="sig-name descname">hard_expiry</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.hard_expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if a password can expire in a hard way. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.max_login_attempts">
<code class="sig-name descname">max_login_attempts</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.max_login_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum logon attempts with an incorrect password within an hour. Valid value range: [0-32]. Default to 5.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.max_password_age">
<code class="sig-name descname">max_password_age</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.max_password_age" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days after which password expires. A value of 0 indicates that the password never expires. Valid value range: [0-1095]. Default to 0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.minimum_password_length">
<code class="sig-name descname">minimum_password_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.minimum_password_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimal required length of password for a user. Valid value range: [8-32]. Default to 12.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.password_reuse_prevention">
<code class="sig-name descname">password_reuse_prevention</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.password_reuse_prevention" title="Permalink to this definition">¶</a></dt>
<dd><p>User is not allowed to use the latest number of passwords specified in this parameter. A value of 0 indicates the password history check policy is disabled. Valid value range: [0-24]. Default to 0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.require_lowercase_characters">
<code class="sig-name descname">require_lowercase_characters</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.require_lowercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the occurrence of a lowercase character in the password is mandatory. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.require_numbers">
<code class="sig-name descname">require_numbers</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.require_numbers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the occurrence of a number in the password is mandatory. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.require_symbols">
<code class="sig-name descname">require_symbols</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.require_symbols" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional Specifies if the occurrence of a special character in the password is mandatory. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.require_uppercase_characters">
<code class="sig-name descname">require_uppercase_characters</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.require_uppercase_characters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the occurrence of an uppercase character in the password is mandatory. Default to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hard_expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_login_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_password_age</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_password_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reuse_prevention</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_lowercase_characters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_numbers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_symbols</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_uppercase_characters</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountPasswordPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hard_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if a password can expire in a hard way. Default to false.</p></li>
<li><p><strong>max_login_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum logon attempts with an incorrect password within an hour. Valid value range: [0-32]. Default to 5.</p></li>
<li><p><strong>max_password_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days after which password expires. A value of 0 indicates that the password never expires. Valid value range: [0-1095]. Default to 0.</p></li>
<li><p><strong>minimum_password_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimal required length of password for a user. Valid value range: [8-32]. Default to 12.</p></li>
<li><p><strong>password_reuse_prevention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User is not allowed to use the latest number of passwords specified in this parameter. A value of 0 indicates the password history check policy is disabled. Valid value range: [0-24]. Default to 0.</p></li>
<li><p><strong>require_lowercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the occurrence of a lowercase character in the password is mandatory. Default to true.</p></li>
<li><p><strong>require_numbers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the occurrence of a number in the password is mandatory. Default to true.</p></li>
<li><p><strong>require_symbols</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional Specifies if the occurrence of a special character in the password is mandatory. Default to true.</p></li>
<li><p><strong>require_uppercase_characters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the occurrence of an uppercase character in the password is mandatory. Default to true.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.AccountPasswordPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AccountPasswordPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.Alias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">Alias</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Alias resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_alicloud.ram.Alias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Alias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Alias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.Alias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetAccountAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetAccountAliasResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetAccountAliasResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetAccountAliasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetAccountAliasesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetAccountAliasesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetRolesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetAccountAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetAccountAliasResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetAccountAliasResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAlias.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetAccountAliasResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetAccountAliasResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetAccountAliasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetAccountAliasesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetAccountAliasesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAliases.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetAccountAliasesResult.account_alias">
<code class="sig-name descname">account_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetAccountAliasesResult.account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of the account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetAccountAliasesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetAccountAliasesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram group names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicies.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetPoliciesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetPoliciesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetPoliciesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetPoliciesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram group names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetPoliciesResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetPoliciesResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetPoliciesResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetPoliciesResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetRolesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRoles.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetRolesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetRolesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetRolesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetRolesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram role IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetRolesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetRolesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram role names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetRolesResult.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetRolesResult.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of roles. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetUsersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetUsersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram user IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetUsersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetUsersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ram user names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GetUsersResult.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ram.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Group resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] comments: Comment of the RAM group. This parameter can have a string of 1 to 128 characters.
:param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] name: Name of the RAM group. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Group.comments">
<code class="sig-name descname">comments</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Group.comments" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment of the RAM group. This parameter can have a string of 1 to 128 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Group.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Group.force" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Group.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM group. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comments</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the RAM group. This parameter can have a string of 1 to 128 characters.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM group. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.GroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GroupMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM Group membership resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>user*names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of user name which will be added to group. Each name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id11"><span class="problematic" id="id12">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GroupMembership.group_name">
<code class="sig-name descname">group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GroupMembership.user_names">
<code class="sig-name descname">user_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership.user_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of user name which will be added to group. Each name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>user*names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of user name which will be added to group. Each name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id15"><span class="problematic" id="id16">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">GroupPolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM Group Policy attachment resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.group_name">
<code class="sig-name descname">group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.policy_type">
<code class="sig-name descname">policy_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupPolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.GroupPolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.GroupPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.LoginProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">LoginProfile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_bind_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM User Login Profile resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mfa_bind_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter indicates whether the MFA needs to be bind when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the RAM user.</p></li>
<li><p><strong>password_reset_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter indicates whether the password needs to be reset when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id19"><span class="problematic" id="id20">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.LoginProfile.mfa_bind_required">
<code class="sig-name descname">mfa_bind_required</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.mfa_bind_required" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter indicates whether the MFA needs to be bind when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.LoginProfile.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of the RAM user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.LoginProfile.password_reset_required">
<code class="sig-name descname">password_reset_required</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.password_reset_required" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter indicates whether the password needs to be reset when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.LoginProfile.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.LoginProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_bind_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoginProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mfa_bind_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter indicates whether the MFA needs to be bind when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the RAM user.</p></li>
<li><p><strong>password_reset_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter indicates whether the password needs to be reset when the user first logs in. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id23"><span class="problematic" id="id24">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.LoginProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.LoginProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.LoginProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statements</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Policy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Description of the RAM policy. This name can have a string of 1 to 1024 characters.
:param pulumi.Input[str] document: Document of the RAM policy. It is required when the <code class="docutils literal notranslate"><span class="pre">statement</span></code> is not specified.
:param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] name: Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.
:param pulumi.Input[list] statements: (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Statements of the RAM policy document. It is required when the <code class="docutils literal notranslate"><span class="pre">document</span></code> is not specified.
:param pulumi.Input[str] version: (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
<p>The <strong>statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of operations for the <code class="docutils literal notranslate"><span class="pre">resource</span></code>. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}:${action_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">oss:ListBuckets</span></code> and <code class="docutils literal notranslate"><span class="pre">ecs:Describe*</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${action_name}</span></code> refers to the name of an api interface which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">action</span></code> is allowed. Valid values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of specific objects which will be authorized. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:${service}:${region}:${account_id}:${relative_id}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ecs:*:*:instance/inst-002</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:oss:*:1234567890000:mybucket</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${region}</span></code> is the region info which can use <code class="docutils literal notranslate"><span class="pre">*</span></code> replace when it is not supplied, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id or you can use <code class="docutils literal notranslate"><span class="pre">*</span></code> to replace, the <code class="docutils literal notranslate"><span class="pre">${relative_id}</span></code> is the resource description section which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.attachment_count">
<code class="sig-name descname">attachment_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.attachment_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy attachment count.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the RAM policy. This name can have a string of 1 to 1024 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.document">
<code class="sig-name descname">document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.document" title="Permalink to this definition">¶</a></dt>
<dd><p>Document of the RAM policy. It is required when the <code class="docutils literal notranslate"><span class="pre">statement</span></code> is not specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.force" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.statements">
<code class="sig-name descname">statements</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.statements" title="Permalink to this definition">¶</a></dt>
<dd><p>(It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Statements of the RAM policy document. It is required when the <code class="docutils literal notranslate"><span class="pre">document</span></code> is not specified.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of operations for the <code class="docutils literal notranslate"><span class="pre">resource</span></code>. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}:${action_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">oss:ListBuckets</span></code> and <code class="docutils literal notranslate"><span class="pre">ecs:Describe*</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${action_name}</span></code> refers to the name of an api interface which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">action</span></code> is allowed. Valid values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of specific objects which will be authorized. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:${service}:${region}:${account_id}:${relative_id}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ecs:*:*:instance/inst-002</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:oss:*:1234567890000:mybucket</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${region}</span></code> is the region info which can use <code class="docutils literal notranslate"><span class="pre">*</span></code> replace when it is not supplied, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id or you can use <code class="docutils literal notranslate"><span class="pre">*</span></code> to replace, the <code class="docutils literal notranslate"><span class="pre">${relative_id}</span></code> is the resource description section which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Policy.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Policy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>(It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachment_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statements</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachment_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The policy attachment count.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the RAM policy. This name can have a string of 1 to 1024 characters.</p></li>
<li><p><strong>document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Document of the RAM policy. It is required when the <code class="docutils literal notranslate"><span class="pre">statement</span></code> is not specified.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Statements of the RAM policy document. It is required when the <code class="docutils literal notranslate"><span class="pre">document</span></code> is not specified.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of operations for the <code class="docutils literal notranslate"><span class="pre">resource</span></code>. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}:${action_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">oss:ListBuckets</span></code> and <code class="docutils literal notranslate"><span class="pre">ecs:Describe*</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${action_name}</span></code> refers to the name of an api interface which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">action</span></code> is allowed. Valid values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of specific objects which will be authorized. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:${service}:${region}:${account_id}:${relative_id}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ecs:*:*:instance/inst-002</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:oss:*:1234567890000:mybucket</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>, <code class="docutils literal notranslate"><span class="pre">ots</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${region}</span></code> is the region info which can use <code class="docutils literal notranslate"><span class="pre">*</span></code> replace when it is not supplied, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id or you can use <code class="docutils literal notranslate"><span class="pre">*</span></code> to replace, the <code class="docutils literal notranslate"><span class="pre">${relative_id}</span></code> is the resource description section which related to the <code class="docutils literal notranslate"><span class="pre">${service}</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Role resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Description of the RAM role. This name can have a string of 1 to 1024 characters.
:param pulumi.Input[str] document: Authorization strategy of the RAM role. It is required when the <code class="docutils literal notranslate"><span class="pre">services</span></code> and <code class="docutils literal notranslate"><span class="pre">ram_users</span></code> are not specified.
:param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] name: Name of the RAM role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “_”, and must not begin with a hyphen.
:param pulumi.Input[list] ram_users: (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of ram users who can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:root</span></code> or <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:user/${user_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890000:root</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890001:user/Mary</span></code>. The <code class="docutils literal notranslate"><span class="pre">${user_name}</span></code> is the name of a RAM user which must exists in the Alicloud account indicated by the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code>.
:param pulumi.Input[list] services: (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of services which can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}.aliyuncs.com</span></code> or <code class="docutils literal notranslate"><span class="pre">${account_id}&#64;${service}.aliyuncs.com</span></code>, such as <code class="docutils literal notranslate"><span class="pre">ecs.aliyuncs.com</span></code> and <code class="docutils literal notranslate"><span class="pre">1234567890000&#64;ots.aliyuncs.com</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code>, <code class="docutils literal notranslate"><span class="pre">apigateway</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id.
:param pulumi.Input[str] version: (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM role policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role arn.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the RAM role. This name can have a string of 1 to 1024 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.document">
<code class="sig-name descname">document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.document" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization strategy of the RAM role. It is required when the <code class="docutils literal notranslate"><span class="pre">services</span></code> and <code class="docutils literal notranslate"><span class="pre">ram_users</span></code> are not specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.force" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.ram_users">
<code class="sig-name descname">ram_users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.ram_users" title="Permalink to this definition">¶</a></dt>
<dd><p>(It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of ram users who can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:root</span></code> or <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:user/${user_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890000:root</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890001:user/Mary</span></code>. The <code class="docutils literal notranslate"><span class="pre">${user_name}</span></code> is the name of a RAM user which must exists in the Alicloud account indicated by the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.role_id">
<code class="sig-name descname">role_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.services">
<code class="sig-name descname">services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.services" title="Permalink to this definition">¶</a></dt>
<dd><p>(It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of services which can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}.aliyuncs.com</span></code> or <code class="docutils literal notranslate"><span class="pre">${account_id}&#64;${service}.aliyuncs.com</span></code>, such as <code class="docutils literal notranslate"><span class="pre">ecs.aliyuncs.com</span></code> and <code class="docutils literal notranslate"><span class="pre">1234567890000&#64;ots.aliyuncs.com</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code>, <code class="docutils literal notranslate"><span class="pre">apigateway</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.Role.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.Role.version" title="Permalink to this definition">¶</a></dt>
<dd><p>(It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM role policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role arn.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the RAM role. This name can have a string of 1 to 1024 characters.</p></li>
<li><p><strong>document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authorization strategy of the RAM role. It is required when the <code class="docutils literal notranslate"><span class="pre">services</span></code> and <code class="docutils literal notranslate"><span class="pre">ram_users</span></code> are not specified.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “_”, and must not begin with a hyphen.</p></li>
<li><p><strong>ram_users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of ram users who can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:root</span></code> or <code class="docutils literal notranslate"><span class="pre">acs:ram::${account_id}:user/${user_name}</span></code>, such as <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890000:root</span></code> and <code class="docutils literal notranslate"><span class="pre">acs:ram::1234567890001:user/Mary</span></code>. The <code class="docutils literal notranslate"><span class="pre">${user_name}</span></code> is the name of a RAM user which must exists in the Alicloud account indicated by the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code>.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role ID.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) List of services which can assume the RAM role. The format of each item in this list is <code class="docutils literal notranslate"><span class="pre">${service}.aliyuncs.com</span></code> or <code class="docutils literal notranslate"><span class="pre">${account_id}&#64;${service}.aliyuncs.com</span></code>, such as <code class="docutils literal notranslate"><span class="pre">ecs.aliyuncs.com</span></code> and <code class="docutils literal notranslate"><span class="pre">1234567890000&#64;ots.aliyuncs.com</span></code>. The <code class="docutils literal notranslate"><span class="pre">${service}</span></code> can be <code class="docutils literal notranslate"><span class="pre">ecs</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code>, <code class="docutils literal notranslate"><span class="pre">apigateway</span></code> and so on, the <code class="docutils literal notranslate"><span class="pre">${account_id}</span></code> refers to someone’s Alicloud account id.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (It has been deprecated from version 1.49.0, and use field ‘document’ to replace.) Version of the RAM role policy document. Valid value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.RoleAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">RoleAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM role attachment resource to bind role for several ECS instances.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of ECS instance’s IDs.</p></li>
<li><p><strong>role*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of role used to bind. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “<a href="#id27"><span class="problematic" id="id28">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.RoleAttachment.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of ECS instance’s IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.RoleAttachment.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of role used to bind. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.RoleAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RoleAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of ECS instance’s IDs.</p></li>
<li><p><strong>role*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of role used to bind. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “<a href="#id31"><span class="problematic" id="id32">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.RoleAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.RoleAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RoleAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">RolePolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM Role attachment resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>role*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM Role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “<a href="#id35"><span class="problematic" id="id36">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.policy_type">
<code class="sig-name descname">policy_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM Role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RolePolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>role*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM Role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“, “<a href="#id39"><span class="problematic" id="id40">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.RolePolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.RolePolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a User resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] comments: Comment of the RAM user. This parameter can have a string of 1 to 128 characters.
:param pulumi.Input[str] display<em>name: Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as “-“,”.”, and must not end with a hyphen.
:param pulumi.Input[str] email: Email of the RAM user.
:param pulumi.Input[bool] force: This parameter is used for resource destroy. Default value is ``false``.
:param pulumi.Input[str] mobile: Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.
:param pulumi.Input[str] name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”</em>”, and must not begin with a hyphen.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.comments">
<code class="sig-name descname">comments</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.comments" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment of the RAM user. This parameter can have a string of 1 to 128 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as “-“,”.”, and must not end with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email of the RAM user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.force" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.mobile">
<code class="sig-name descname">mobile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.mobile" title="Permalink to this definition">¶</a></dt>
<dd><p>Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.User.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comments</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the RAM user. This parameter can have a string of 1 to 128 characters.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user which for display. This name can have a string of 1 to 128 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as “-“,”.”, and must not end with a hyphen.</p>
</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email of the RAM user.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is used for resource destroy. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id43"><span class="problematic" id="id44">*</span></a>”, and must not begin with a hyphen.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">UserPolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a RAM User Policy attachment resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id47"><span class="problematic" id="id48">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.policy_type">
<code class="sig-name descname">policy_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin with a hyphen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen “-“, and must not begin with a hyphen.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the RAM policy. It must be <code class="docutils literal notranslate"><span class="pre">Custom</span></code> or <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>user*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id51"><span class="problematic" id="id52">*</span></a>”, and must not begin with a hyphen.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ram.UserPolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.UserPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_account_alias">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_account_alias</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_account_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_account_aliases">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_account_aliases</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_account_aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides an alias for the Alibaba Cloud account.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_groups">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of RAM Groups in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter the returned groups by their names.</p></li>
<li><p><strong>policy_name</strong> (<em>str</em>) – Filter the results by a specific policy name. If you set this parameter without setting <code class="docutils literal notranslate"><span class="pre">policy_type</span></code>, it will be automatically set to <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>policy_type</strong> (<em>str</em>) – Filter the results by a specific policy type. Valid items are <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">System</span></code>. If you set this parameter, you must set <code class="docutils literal notranslate"><span class="pre">policy_name</span></code> as well.</p></li>
<li><p><strong>user_name</strong> (<em>str</em>) – Filter the results by a specific the user name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_policies">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_policies</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of RAM policies in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_name</strong> (<em>str</em>) – Filter results by a specific group name. Returned policies are attached to the specified group.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting policies by name.</p></li>
<li><p><strong>role_name</strong> (<em>str</em>) – Filter results by a specific role name. Returned policies are attached to the specified role.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Filter results by a specific policy type. Valid values are <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
<li><p><strong>user_name</strong> (<em>str</em>) – Filter results by a specific user name. Returned policies are attached to the specified user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_roles">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_roles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of RAM Roles in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – <ul>
<li><p>A list of ram role IDs.</p></li>
</ul>
</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the role name.</p></li>
<li><p><strong>policy_name</strong> (<em>str</em>) – Filter results by a specific policy name. If you set this parameter without setting <code class="docutils literal notranslate"><span class="pre">policy_type</span></code>, the later will be automatically set to <code class="docutils literal notranslate"><span class="pre">System</span></code>. The resulting roles will be attached to the specified policy.</p></li>
<li><p><strong>policy_type</strong> (<em>str</em>) – Filter results by a specific policy type. Valid values are <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">System</span></code>. If you set this parameter, you must set <code class="docutils literal notranslate"><span class="pre">policy_name</span></code> as well.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ram.get_users">
<code class="sig-prename descclassname">pulumi_alicloud.ram.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ram.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of RAM users in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_name</strong> (<em>str</em>) – Filter results by a specific group name. Returned users are in the specified group.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – <ul>
<li><p>A list of ram user IDs.</p></li>
</ul>
</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting users by their names.</p></li>
<li><p><strong>policy_name</strong> (<em>str</em>) – Filter results by a specific policy name. If you set this parameter without setting <code class="docutils literal notranslate"><span class="pre">policy_type</span></code>, the later will be automatically set to <code class="docutils literal notranslate"><span class="pre">System</span></code>. Returned users are attached to the specified policy.</p></li>
<li><p><strong>policy_type</strong> (<em>str</em>) – Filter results by a specific policy type. Valid values are <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">System</span></code>. If you set this parameter, you must set <code class="docutils literal notranslate"><span class="pre">policy_name</span></code> as well.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
