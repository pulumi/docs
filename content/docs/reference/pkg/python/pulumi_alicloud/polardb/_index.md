---
title: Module polardb
title_tag: Module polardb | Package pulumi_alicloud | Python SDK
linktitle: polardb
notitle: true
---

<div class="section" id="polardb">
<h1>polardb<a class="headerlink" href="#polardb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.polardb"></span><dl class="class">
<dt id="pulumi_alicloud.polardb.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_description=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB account resource and used to manage databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.67.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id3"><span class="problematic" id="id4">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p></li>
<li><p><strong>account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account type, Valid values are <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">Super</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Normal</span></code>.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.account_description">
<code class="sig-name descname">account_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.account_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.account_password">
<code class="sig-name descname">account_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.account_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.account_type">
<code class="sig-name descname">account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Account type, Valid values are <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">Super</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Normal</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster in which account belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Account.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Account.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_description=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id8"><span class="problematic" id="id9">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p></li>
<li><p><strong>account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account type, Valid values are <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">Super</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Normal</span></code>.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.AccountPrivilege">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AccountPrivilege</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_privilege=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_names=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB account privilege resource and used to grant several database some access privilege. A database can be granted by multiple account.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.67.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A specified account name.</p></li>
<li><p><strong>account_privilege</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The privilege of one account access database. Valid values: [“ReadOnly”, “ReadWrite”]. Default to “ReadOnly”.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>db_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of specified database name.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A specified account name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.account_privilege">
<code class="sig-name descname">account_privilege</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.account_privilege" title="Permalink to this definition">¶</a></dt>
<dd><p>The privilege of one account access database. Valid values: [“ReadOnly”, “ReadWrite”]. Default to “ReadOnly”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster in which account belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.db_names">
<code class="sig-name descname">db_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.db_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of specified database name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_privilege=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountPrivilege resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A specified account name.</p></li>
<li><p><strong>account_privilege</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The privilege of one account access database. Valid values: [“ReadOnly”, “ReadWrite”]. Default to “ReadOnly”.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>db_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of specified database name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.AccountPrivilege.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.AccountPrivilege.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AccountPrivilege.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.AwaitableGetAccountsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AwaitableGetAccountsResult</code><span class="sig-paren">(</span><em class="sig-param">accounts=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AwaitableGetAccountsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">db_type=None</em>, <em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.AwaitableGetDatabasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AwaitableGetDatabasesResult</code><span class="sig-paren">(</span><em class="sig-param">databases=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AwaitableGetDatabasesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.AwaitableGetEndpointsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AwaitableGetEndpointsResult</code><span class="sig-paren">(</span><em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_endpoint_id=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AwaitableGetEndpointsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.BackupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">BackupPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">preferred_backup_periods=None</em>, <em class="sig-param">preferred_backup_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BackupPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] db_cluster_id: The Id of cluster that can run database.
:param pulumi.Input[list] preferred_backup_periods: PolarDB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].
:param pulumi.Input[str] preferred_backup_time: PolarDB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.BackupPolicy.backup_retention_period">
<code class="sig-name descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster backup retention days, Fixed for 7 days, not modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.BackupPolicy.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.BackupPolicy.preferred_backup_periods">
<code class="sig-name descname">preferred_backup_periods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.preferred_backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>PolarDB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.BackupPolicy.preferred_backup_time">
<code class="sig-name descname">preferred_backup_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.preferred_backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>PolarDB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.BackupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_retention_period=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">preferred_backup_periods=None</em>, <em class="sig-param">preferred_backup_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackupPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster backup retention days, Fixed for 7 days, not modified.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>preferred_backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – PolarDB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].</p></li>
<li><p><strong>preferred_backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PolarDB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.BackupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.BackupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.BackupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_renew_period=None</em>, <em class="sig-param">db_node_class=None</em>, <em class="sig-param">db_type=None</em>, <em class="sig-param">db_version=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">maintain_time=None</em>, <em class="sig-param">modify_type=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">pay_type=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewal_status=None</em>, <em class="sig-param">security_ips=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB cluster resource. A PolarDB cluster is an isolated database
environment in the cloud. A PolarDB cluster can contain multiple user-created
databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.66.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p></li>
<li><p><strong>db_node_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db_node_class of cluster node.</p></li>
<li><p><strong>db_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Value options: MySQL, Oracle, PostgreSQL.</p></li>
<li><p><strong>db_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database version. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/98169.html">CreateDBCluster</a> <code class="docutils literal notranslate"><span class="pre">DBVersion</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of cluster.</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
<li><p><strong>modify_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use as <code class="docutils literal notranslate"><span class="pre">db_node_class</span></code> change class , define upgrade or downgrade.  Valid values are <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>, <code class="docutils literal notranslate"><span class="pre">Downgrade</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of parameters needs to be set after DB cluster was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Currently, the resource can not supports change pay type.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB cluster (in month). It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">AutoRenewal</span></code>, <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>.</p></li>
<li><p><strong>security_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB cluster. it supports multiple zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.db_node_class">
<code class="sig-name descname">db_node_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.db_node_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The db_node_class of cluster node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.db_type">
<code class="sig-name descname">db_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.db_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type. Value options: MySQL, Oracle, PostgreSQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.db_version">
<code class="sig-name descname">db_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.db_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/98169.html">CreateDBCluster</a> <code class="docutils literal notranslate"><span class="pre">DBVersion</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.maintain_time">
<code class="sig-name descname">maintain_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.maintain_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.modify_type">
<code class="sig-name descname">modify_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.modify_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Use as <code class="docutils literal notranslate"><span class="pre">db_node_class</span></code> change class , define upgrade or downgrade.  Valid values are <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>, <code class="docutils literal notranslate"><span class="pre">Downgrade</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of parameters needs to be set after DB cluster was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.pay_type">
<code class="sig-name descname">pay_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Currently, the resource can not supports change pay type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy DB cluster (in month). It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.renewal_status">
<code class="sig-name descname">renewal_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.renewal_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">AutoRenewal</span></code>, <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.security_ips">
<code class="sig-name descname">security_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.security_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Cluster.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB cluster. it supports multiple zone.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_renew_period=None</em>, <em class="sig-param">db_node_class=None</em>, <em class="sig-param">db_type=None</em>, <em class="sig-param">db_version=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">maintain_time=None</em>, <em class="sig-param">modify_type=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">pay_type=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewal_status=None</em>, <em class="sig-param">security_ips=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p></li>
<li><p><strong>db_node_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db_node_class of cluster node.</p></li>
<li><p><strong>db_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Value options: MySQL, Oracle, PostgreSQL.</p></li>
<li><p><strong>db_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/98169.html">CreateDBCluster</a> <code class="docutils literal notranslate"><span class="pre">DBVersion</span></code>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of cluster.</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
<li><p><strong>modify_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use as <code class="docutils literal notranslate"><span class="pre">db_node_class</span></code> change class , define upgrade or downgrade.  Valid values are <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>, <code class="docutils literal notranslate"><span class="pre">Downgrade</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Upgrade</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of parameters needs to be set after DB cluster was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p>
</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Currently, the resource can not supports change pay type.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB cluster (in month). It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">AutoRenewal</span></code>, <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>.</p></li>
<li><p><strong>security_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB cluster. it supports multiple zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">character_set_name=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_description=None</em>, <em class="sig-param">db_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB database resource. A DB database deployed in a DB cluster. A DB cluster can own multiple databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.66.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>character_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set. The value range is limited to the following: [ utf8, gbk, latin1, utf8mb4, Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ], default is “utf8” (<code class="docutils literal notranslate"><span class="pre">utf8mb4</span></code> only supports versions 5.5 and 5.6).</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>db*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id17"><span class="problematic" id="id18">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letterand have no more than 64 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Database.character_set_name">
<code class="sig-name descname">character_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Database.character_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Character set. The value range is limited to the following: [ utf8, gbk, latin1, utf8mb4, Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ], default is “utf8” (<code class="docutils literal notranslate"><span class="pre">utf8mb4</span></code> only supports versions 5.5 and 5.6).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Database.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Database.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Database.db_description">
<code class="sig-name descname">db_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Database.db_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Database.db_name">
<code class="sig-name descname">db_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Database.db_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letterand have no more than 64 characters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">character_set_name=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_description=None</em>, <em class="sig-param">db_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>character_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set. The value range is limited to the following: [ utf8, gbk, latin1, utf8mb4, Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ], default is “utf8” (<code class="docutils literal notranslate"><span class="pre">utf8mb4</span></code> only supports versions 5.5 and 5.6).</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>db*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id21"><span class="problematic" id="id22">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letterand have no more than 64 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_add_new_nodes=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">read_write_mode=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB endpoint resource to allocate an Internet endpoint string for PolarDB instance.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>NOTE:</strong> Available in v1.80.0+. Each PolarDB instance will allocate a intranet connection string automatically and its prefix is Cluster ID.</dt><dd><p>To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_add_new_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the new node automatically joins the default cluster address. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>endpoint_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Advanced configuration of the cluster address.</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of endpoint. Valid value: <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.</p></li>
<li><p><strong>read_write_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read or write mode. Valid values are <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.auto_add_new_nodes">
<code class="sig-name descname">auto_add_new_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.auto_add_new_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the new node automatically joins the default cluster address. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.endpoint_config">
<code class="sig-name descname">endpoint_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.endpoint_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Advanced configuration of the cluster address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.endpoint_type">
<code class="sig-name descname">endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of endpoint. Valid value: <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.nodes">
<code class="sig-name descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.Endpoint.read_write_mode">
<code class="sig-name descname">read_write_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.read_write_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Read or write mode. Valid values are <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_add_new_nodes=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">read_write_mode=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_add_new_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the new node automatically joins the default cluster address. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>endpoint_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Advanced configuration of the cluster address.</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of endpoint. Valid value: <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.</p></li>
<li><p><strong>read_write_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read or write mode. Valid values are <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.EndpointAddress">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">EndpointAddress</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_prefix=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_endpoint_id=None</em>, <em class="sig-param">net_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a PolarDB endpoint address resource to allocate an Internet endpoint address string for PolarDB instance.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>NOTE:</strong> Available in v1.68.0+. Each PolarDB instance will allocate a intranet connection string automatically and its prefix is Cluster ID.</dt><dd><p>To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><db_endpoint_id></span> + ‘tf’.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>db_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of endpoint that can run database.</p></li>
<li><p><strong>net_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection net type. Valid value: <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Public</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.connection_prefix">
<code class="sig-name descname">connection_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.connection_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><db_endpoint_id></span> + ‘tf’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection cluster or endpoint string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.db_endpoint_id">
<code class="sig-name descname">db_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.db_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of endpoint that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ip address of connection string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.net_type">
<code class="sig-name descname">net_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.net_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet connection net type. Valid value: <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Public</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.EndpointAddress.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection cluster or endpoint port.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.EndpointAddress.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_prefix=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_endpoint_id=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">net_type=None</em>, <em class="sig-param">port=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointAddress resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><db_endpoint_id></span> + ‘tf’.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection cluster or endpoint string.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster that can run database.</p></li>
<li><p><strong>db_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of endpoint that can run database.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ip address of connection string.</p></li>
<li><p><strong>net_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection net type. Valid value: <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Public</span></code>. Currently supported only <code class="docutils literal notranslate"><span class="pre">Public</span></code>.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection cluster or endpoint port.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.polardb.EndpointAddress.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.EndpointAddress.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.EndpointAddress.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.polardb.GetAccountsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">GetAccountsResult</code><span class="sig-paren">(</span><em class="sig-param">accounts=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.GetAccountsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccounts.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetAccountsResult.accounts">
<code class="sig-name descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetAccountsResult.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of PolarDB cluster accounts. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetAccountsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetAccountsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetAccountsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetAccountsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>Account name of the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">db_type=None</em>, <em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of PolarDB clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.db_type">
<code class="sig-name descname">db_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.db_type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Primary</span></code> for primary cluster, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> for read-only cluster, <code class="docutils literal notranslate"><span class="pre">Guard</span></code> for disaster recovery cluster, and <code class="docutils literal notranslate"><span class="pre">Temp</span></code> for temporary cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.descriptions">
<code class="sig-name descname">descriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of RDS cluster descriptions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of RDS cluster IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetClustersResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetClustersResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.GetDatabasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">GetDatabasesResult</code><span class="sig-paren">(</span><em class="sig-param">databases=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.GetDatabasesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabases.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetDatabasesResult.databases">
<code class="sig-name descname">databases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetDatabasesResult.databases" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of PolarDB cluster databases. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetDatabasesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetDatabasesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetDatabasesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetDatabasesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>database name of the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.GetEndpointsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">GetEndpointsResult</code><span class="sig-paren">(</span><em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_endpoint_id=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.GetEndpointsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEndpoints.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetEndpointsResult.db_endpoint_id">
<code class="sig-name descname">db_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetEndpointsResult.db_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetEndpointsResult.endpoints">
<code class="sig-name descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetEndpointsResult.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of PolarDB cluster endpoints. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetEndpointsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetEndpointsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.polardb.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.polardb.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.polardb.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.polardb.get_accounts">
<code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">get_accounts</code><span class="sig-paren">(</span><em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.get_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">polardb.getAccounts</span></code> data source provides a collection of PolarDB cluster database account available in Alibaba Cloud account.
Filters support regular expression for the account name, searches by clusterId.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.70.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>db_cluster_id</strong> (<em>str</em>) – The polarDB cluster ID.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by account name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.polardb.get_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param">db_type=None</em>, <em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">polardb.getClusters</span></code> data source provides a collection of PolarDB clusters available in Alibaba Cloud account.
Filters support regular expression for the cluster description, searches by tags, and other filters which are listed below.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.66.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>db_type</strong> (<em>str</em>) – Database type. Options are <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">Oracle</span></code> and <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>. If no value is specified, all types are returned.</p></li>
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter results by cluster description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of PolarDB cluster IDs.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – status of the cluster.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.polardb.get_databases">
<code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">get_databases</code><span class="sig-paren">(</span><em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.get_databases" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">polardb.getDatabases</span></code> data source provides a collection of PolarDB cluster database available in Alibaba Cloud account.
Filters support regular expression for the database name, searches by clusterId.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.70.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>db_cluster_id</strong> (<em>str</em>) – The polarDB cluster ID.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by database name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.polardb.get_endpoints">
<code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">get_endpoints</code><span class="sig-paren">(</span><em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">db_endpoint_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.get_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">polardb.getEndpoints</span></code> data source provides a collection of PolarDB endpoints available in Alibaba Cloud account.
Filters support regular expression for the cluster name, searches by clusterId, and other filters which are listed below.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.68.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>db_cluster_id</strong> (<em>str</em>) – PolarDB cluster ID.</p></li>
<li><p><strong>db_endpoint_id</strong> (<em>str</em>) – endpoint of the cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.polardb.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.polardb.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.polardb.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for PolarDB that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.74.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch PolarDB instances.</p>
</dd>
</dl>
</dd></dl>

</div>
