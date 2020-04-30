---
title: Module rds
title_tag: Module rds | Package pulumi_alicloud | Python SDK
linktitle: rds
notitle: true
---

<div class="section" id="rds">
<h1>rds<a class="headerlink" href="#rds" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.rds"></span><dl class="py class">
<dt id="pulumi_alicloud.rds.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS account resource and used to manage databases.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id3"><span class="problematic" id="id4">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Privilege type of account.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Normal</span><span class="p">:</span> <span class="n">Common</span> <span class="n">privilege</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Super</span><span class="p">:</span> <span class="n">High</span> <span class="n">privilege</span><span class="o">.</span>
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance in which account belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Account.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Account.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Privilege type of account.</p>
<ul class="simple">
<li><p>Normal: Common privilege.</p></li>
<li><p>Super: High privilege.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id8"><span class="problematic" id="id9">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Privilege type of account.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Normal</span><span class="p">:</span> <span class="n">Common</span> <span class="n">privilege</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Super</span><span class="p">:</span> <span class="n">High</span> <span class="n">privilege</span><span class="o">.</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.AccountPrivilege">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">AccountPrivilege</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privilege</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS account privilege resource and used to grant several database some access privilege. A database can be granted by multiple account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A specified account name.</p></li>
<li><p><strong>db_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of specified database name.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance in which account belongs.</p></li>
<li><p><strong>privilege</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The privilege of one account access database. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">ReadOnly</span><span class="p">:</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span><span class="p">,</span> <span class="n">MariaDB</span> <span class="ow">and</span> <span class="n">SQL</span> <span class="n">Server</span>
<span class="o">-</span> <span class="n">ReadWrite</span><span class="p">:</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span><span class="p">,</span> <span class="n">MariaDB</span> <span class="ow">and</span> <span class="n">SQL</span> <span class="n">Server</span>
<span class="o">-</span> <span class="n">DDLOnly</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span> <span class="ow">and</span> <span class="n">MariaDB</span>
<span class="o">-</span> <span class="n">DMLOnly</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span> <span class="ow">and</span> <span class="n">MariaDB</span>
<span class="o">-</span> <span class="n">DBOwner</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">SQL</span> <span class="n">Server</span> <span class="ow">and</span> <span class="n">PostgreSQL</span><span class="o">.</span>
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.AccountPrivilege.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A specified account name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.AccountPrivilege.db_names">
<code class="sig-name descname">db_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.db_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of specified database name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.AccountPrivilege.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance in which account belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.AccountPrivilege.privilege">
<code class="sig-name descname">privilege</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.privilege" title="Permalink to this definition">¶</a></dt>
<dd><p>The privilege of one account access database. Valid values:</p>
<ul class="simple">
<li><p>ReadOnly: This value is only for MySQL, MariaDB and SQL Server</p></li>
<li><p>ReadWrite: This value is only for MySQL, MariaDB and SQL Server</p></li>
<li><p>DDLOnly: (Available in 1.64.0+) This value is only for MySQL and MariaDB</p></li>
<li><p>DMLOnly: (Available in 1.64.0+) This value is only for MySQL and MariaDB</p></li>
<li><p>DBOwner: (Available in 1.64.0+) This value is only for SQL Server and PostgreSQL.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.AccountPrivilege.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privilege</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountPrivilege resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A specified account name.</p></li>
<li><p><strong>db_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of specified database name.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance in which account belongs.</p></li>
<li><p><strong>privilege</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The privilege of one account access database. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">ReadOnly</span><span class="p">:</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span><span class="p">,</span> <span class="n">MariaDB</span> <span class="ow">and</span> <span class="n">SQL</span> <span class="n">Server</span>
<span class="o">-</span> <span class="n">ReadWrite</span><span class="p">:</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span><span class="p">,</span> <span class="n">MariaDB</span> <span class="ow">and</span> <span class="n">SQL</span> <span class="n">Server</span>
<span class="o">-</span> <span class="n">DDLOnly</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span> <span class="ow">and</span> <span class="n">MariaDB</span>
<span class="o">-</span> <span class="n">DMLOnly</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">MySQL</span> <span class="ow">and</span> <span class="n">MariaDB</span>
<span class="o">-</span> <span class="n">DBOwner</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.64</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">only</span> <span class="k">for</span> <span class="n">SQL</span> <span class="n">Server</span> <span class="ow">and</span> <span class="n">PostgreSQL</span><span class="o">.</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.AccountPrivilege.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.AccountPrivilege.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AccountPrivilege.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.AwaitableGetInstanceClassesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">AwaitableGetInstanceClassesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_classes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AwaitableGetInstanceClassesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.AwaitableGetInstanceEnginesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">AwaitableGetInstanceEnginesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_engines</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AwaitableGetInstanceEnginesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.BackupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">BackupPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_keep_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_keep_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backup_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">high_space_usage_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_log_retention_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_log_retention_space</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS instance backup policy resource and used to configure instance backup policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Each DB instance has a backup policy and it will be set default values when destroying the resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>archive_backup_keep_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance archive backup keep count. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code> Valid values: [1-31]. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByWeek</span></code> Valid values: [1-7].</p></li>
<li><p><strong>archive_backup_keep_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance archive backup keep policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values are <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>, <code class="docutils literal notranslate"><span class="pre">KeepAll</span></code>.</p></li>
<li><p><strong>archive_backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance archive backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values: [30-1095], and <code class="docutils literal notranslate"><span class="pre">archive_backup_retention_period</span></code> must larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code> 730.</p></li>
<li><p><strong>backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘preferred_backup_period’ instead.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.</p></li>
<li><p><strong>backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘preferred_backup_time’ instead.</p></li>
<li><p><strong>compress_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compress type of instance policy. Valid values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><strong>enable_backup_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to backup instance log. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Note: The ‘Basic Edition’ category Rds instance does not support setting log backup. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/48980.htm">What is Basic Edition</a>.</p></li>
<li><p><strong>high_space_usage_protection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance high space usage protection policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>local_log_retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup local retention hours. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [0-7*24].</p></li>
<li><p><strong>local_log_retention_space</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup local retention space. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [5-50].</p></li>
<li><p><strong>log_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It has been deprecated from version 1.68.0, and use field ‘enable_backup_log’ instead.</p></li>
<li><p><strong>log_backup_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance log backup frequency. Valid when the instance engine is <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">LogInterval</span></code>.</p></li>
<li><p><strong>log_backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Valid values: [7-730]. Default to 7. It cannot be larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code>.</p></li>
<li><p><strong>log_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘log_backup_retention_period’ instead.</p></li>
<li><p><strong>preferred_backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday”, “Sunday”].</p></li>
<li><p><strong>preferred_backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘backup_retention_period’ instead.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.archive_backup_keep_count">
<code class="sig-name descname">archive_backup_keep_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.archive_backup_keep_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance archive backup keep count. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code> Valid values: [1-31]. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByWeek</span></code> Valid values: [1-7].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.archive_backup_keep_policy">
<code class="sig-name descname">archive_backup_keep_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.archive_backup_keep_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance archive backup keep policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values are <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>, <code class="docutils literal notranslate"><span class="pre">KeepAll</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.archive_backup_retention_period">
<code class="sig-name descname">archive_backup_retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.archive_backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance archive backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values: [30-1095], and <code class="docutils literal notranslate"><span class="pre">archive_backup_retention_period</span></code> must larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code> 730.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.backup_periods">
<code class="sig-name descname">backup_periods</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.69.0, and use field ‘preferred_backup_period’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.backup_retention_period">
<code class="sig-name descname">backup_retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.backup_time">
<code class="sig-name descname">backup_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.69.0, and use field ‘preferred_backup_time’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.compress_type">
<code class="sig-name descname">compress_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.compress_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The compress type of instance policy. Valid values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.enable_backup_log">
<code class="sig-name descname">enable_backup_log</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.enable_backup_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to backup instance log. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Note: The ‘Basic Edition’ category Rds instance does not support setting log backup. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/48980.htm">What is Basic Edition</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.high_space_usage_protection">
<code class="sig-name descname">high_space_usage_protection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.high_space_usage_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance high space usage protection policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance that can run database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.local_log_retention_hours">
<code class="sig-name descname">local_log_retention_hours</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.local_log_retention_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup local retention hours. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [0-7*24].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.local_log_retention_space">
<code class="sig-name descname">local_log_retention_space</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.local_log_retention_space" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup local retention space. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [5-50].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.log_backup">
<code class="sig-name descname">log_backup</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.log_backup" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.68.0, and use field ‘enable_backup_log’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.log_backup_frequency">
<code class="sig-name descname">log_backup_frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.log_backup_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup frequency. Valid when the instance engine is <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">LogInterval</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.log_backup_retention_period">
<code class="sig-name descname">log_backup_retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.log_backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Valid values: [7-730]. Default to 7. It cannot be larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.log_retention_period">
<code class="sig-name descname">log_retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.log_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.69.0, and use field ‘log_backup_retention_period’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.preferred_backup_periods">
<code class="sig-name descname">preferred_backup_periods</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.preferred_backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday”, “Sunday”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.preferred_backup_time">
<code class="sig-name descname">preferred_backup_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.preferred_backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.BackupPolicy.retention_period">
<code class="sig-name descname">retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.69.0, and use field ‘backup_retention_period’ instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.BackupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_keep_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_keep_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backup_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">high_space_usage_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_log_retention_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_log_retention_space</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_backup_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_backup_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackupPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>archive_backup_keep_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance archive backup keep count. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code> Valid values: [1-31]. When <code class="docutils literal notranslate"><span class="pre">archive_backup_keep_policy</span></code> is <code class="docutils literal notranslate"><span class="pre">ByWeek</span></code> Valid values: [1-7].</p></li>
<li><p><strong>archive_backup_keep_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance archive backup keep policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values are <code class="docutils literal notranslate"><span class="pre">ByMonth</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>, <code class="docutils literal notranslate"><span class="pre">KeepAll</span></code>.</p></li>
<li><p><strong>archive_backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance archive backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and instance is mysql local disk. Valid values: [30-1095], and <code class="docutils literal notranslate"><span class="pre">archive_backup_retention_period</span></code> must larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code> 730.</p></li>
<li><p><strong>backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘preferred_backup_period’ instead.</p></li>
<li><p><strong>backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.</p></li>
<li><p><strong>backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘preferred_backup_time’ instead.</p></li>
<li><p><strong>compress_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compress type of instance policy. Valid values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><strong>enable_backup_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether to backup instance log. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Note: The ‘Basic Edition’ category Rds instance does not support setting log backup. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/48980.htm">What is Basic Edition</a>.</p>
</p></li>
<li><p><strong>high_space_usage_protection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance high space usage protection policy. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Enable</span></code>, <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>local_log_retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup local retention hours. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [0-7*24].</p></li>
<li><p><strong>local_log_retention_space</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup local retention space. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Valid values: [5-50].</p></li>
<li><p><strong>log_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It has been deprecated from version 1.68.0, and use field ‘enable_backup_log’ instead.</p></li>
<li><p><strong>log_backup_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance log backup frequency. Valid when the instance engine is <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">LogInterval</span></code>.</p></li>
<li><p><strong>log_backup_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup retention days. Valid when the <code class="docutils literal notranslate"><span class="pre">enable_backup_log</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Valid values: [7-730]. Default to 7. It cannot be larger than <code class="docutils literal notranslate"><span class="pre">backup_retention_period</span></code>.</p></li>
<li><p><strong>log_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘log_backup_retention_period’ instead.</p></li>
<li><p><strong>preferred_backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday”, “Sunday”].</p></li>
<li><p><strong>preferred_backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from version 1.69.0, and use field ‘backup_retention_period’ instead.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.BackupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.BackupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.BackupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS connection resource to allocate an Internet connection string for RDS instance.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>NOTE:</strong> Each RDS instance will allocate a intranet connnection string automatically and its prifix is RDS instance ID.</dt><dd><p>To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘tf’.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection port. Valid value: [3001-3999]. Default to 3306.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Connection.connection_prefix">
<code class="sig-name descname">connection_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Connection.connection_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘tf’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Connection.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Connection.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection instance string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Connection.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Connection.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance that can run database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Connection.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Connection.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ip address of connection string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Connection.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Connection.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet connection port. Valid value: [3001-3999]. Default to 3306.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘tf’.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection instance string.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ip address of connection string.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection port. Valid value: [3001-3999]. Default to 3306.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">character_set</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS database resource. A DB database deployed in a DB instance. A DB instance can own multiple databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource does not support creating ‘PPAS’ database. You have to login RDS instance to create manually.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>character_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set. The value range is limited to the following:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- MySQL: [ utf8, gbk, latin1, utf8mb4 ] \(`utf8mb4` only supports versions 5.5 and 5.6\).
- SQLServer: [ Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ]
- PostgreSQL: [ KOI8U、UTF8、WIN866、WIN874、WIN1250、WIN1251、WIN1252、WIN1253、WIN1254、WIN1255、WIN1256、WIN1257、WIN1258、EUC_CN、EUC_KR、EUC_TW、EUC_JP、EUC_JIS_2004、KOI8R、MULE_INTERNAL、LATIN1、LATIN2、LATIN3、LATIN4、LATIN5、LATIN6、LATIN7、LATIN8、LATIN9、LATIN10、ISO_8859_5、ISO_8859_6、ISO_8859_7、ISO_8859_8、SQL_ASCII ]
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter
and have no more than 64 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Database.character_set">
<code class="sig-name descname">character_set</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Database.character_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Character set. The value range is limited to the following:</p>
<ul class="simple">
<li><p>MySQL: [ utf8, gbk, latin1, utf8mb4 ] (<code class="docutils literal notranslate"><span class="pre">utf8mb4</span></code> only supports versions 5.5 and 5.6).</p></li>
<li><p>SQLServer: [ Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ]</p></li>
<li><p>PostgreSQL: [ KOI8U、UTF8、WIN866、WIN874、WIN1250、WIN1251、WIN1252、WIN1253、WIN1254、WIN1255、WIN1256、WIN1257、WIN1258、EUC_CN、EUC_KR、EUC_TW、EUC_JP、EUC_JIS_2004、KOI8R、MULE_INTERNAL、LATIN1、LATIN2、LATIN3、LATIN4、LATIN5、LATIN6、LATIN7、LATIN8、LATIN9、LATIN10、ISO_8859_5、ISO_8859_6、ISO_8859_7、ISO_8859_8、SQL_ASCII ]</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Database.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Database.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Database.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Database.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance that can run database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Database.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter
and have no more than 64 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">character_set</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>character_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set. The value range is limited to the following:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- MySQL: [ utf8, gbk, latin1, utf8mb4 ] \(`utf8mb4` only supports versions 5.5 and 5.6\).
- SQLServer: [ Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ]
- PostgreSQL: [ KOI8U、UTF8、WIN866、WIN874、WIN1250、WIN1251、WIN1252、WIN1253、WIN1254、WIN1255、WIN1256、WIN1257、WIN1258、EUC_CN、EUC_KR、EUC_TW、EUC_JP、EUC_JIS_2004、KOI8R、MULE_INTERNAL、LATIN1、LATIN2、LATIN3、LATIN4、LATIN5、LATIN6、LATIN7、LATIN8、LATIN9、LATIN10、ISO_8859_5、ISO_8859_6、ISO_8859_7、ISO_8859_8、SQL_ASCII ]
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter
and have no more than 64 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.GetInstanceClassesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">GetInstanceClassesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_classes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceClassesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceClasses.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceClassesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceClassesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceClassesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceClassesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(Available in 1.60.0+) A list of Rds instance class codes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceClassesResult.instance_classes">
<code class="sig-name descname">instance_classes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceClassesResult.instance_classes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Rds available resource. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.GetInstanceEnginesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">GetInstanceEnginesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_engines</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceEnginesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceEngines.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceEnginesResult.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceEnginesResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceEnginesResult.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceEnginesResult.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>DB Instance version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceEnginesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceEnginesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstanceEnginesResult.instance_engines">
<code class="sig-name descname">instance_engines</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstanceEnginesResult.instance_engines" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Rds available resource. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.connection_mode">
<code class="sig-name descname">connection_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.connection_mode" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Standard</span></code> for standard access mode and <code class="docutils literal notranslate"><span class="pre">Safe</span></code> for high security access mode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.db_type">
<code class="sig-name descname">db_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.db_type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Primary</span></code> for primary instance, <code class="docutils literal notranslate"><span class="pre">Readonly</span></code> for read-only instance, <code class="docutils literal notranslate"><span class="pre">Guard</span></code> for disaster recovery instance, and <code class="docutils literal notranslate"><span class="pre">Temp</span></code> for temporary instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.engine">
<code class="sig-name descname">engine</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type. Options are <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code> and <code class="docutils literal notranslate"><span class="pre">PPAS</span></code>. If no value is specified, all types are returned.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of RDS instance IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of RDS instances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of RDS instance names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC the instance belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetInstancesResult.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetInstancesResult.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VSwitch the instance belongs to.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.rds.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_upgrade_minor_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_restart</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_ip_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_collector_config_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_collector_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS instance resource. A DB instance is an isolated database
environment in the cloud. A DB instance can contain multiple user-created
databases.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:[1~12], Default to 1.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The upgrade method to use. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Auto</span><span class="p">:</span> <span class="n">Instances</span> <span class="n">are</span> <span class="n">automatically</span> <span class="n">upgraded</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">minor</span> <span class="n">version</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Manual</span><span class="p">:</span> <span class="n">Instances</span> <span class="n">are</span> <span class="n">forcibly</span> <span class="n">upgraded</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">minor</span> <span class="n">version</span> <span class="n">when</span> <span class="n">the</span> <span class="n">current</span> <span class="n">version</span> <span class="ow">is</span> <span class="n">unpublished</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>db_instance_storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The storage type of the instance. Valid values:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">local_ssd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">local</span> <span class="n">SSDs</span><span class="o">.</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">recommended</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">standard</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd2</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd3</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p></li>
<li><p><strong>force_restart</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set it to true to make some parameter efficient when modifying them. Default to false.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">Prepaid</span></code>, <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>. Currently, the resource only supports PostPaid to PrePaid.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined DB instance storage space. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
<li><p><strong>monitoring_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from 1.69.0 and use <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> instead.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – , Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.</p></li>
<li><p><strong>security_ip_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">safety</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">normal</span></code>. support <code class="docutils literal notranslate"><span class="pre">safety</span></code> switch to high security access mode</p></li>
<li><p><strong>security_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>sql_collector_config_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The sql collector keep time of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">180</span></code>, <code class="docutils literal notranslate"><span class="pre">365</span></code>, <code class="docutils literal notranslate"><span class="pre">1095</span></code>, <code class="docutils literal notranslate"><span class="pre">1825</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>sql_collector_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sql collector status of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:[1~12], Default to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.auto_upgrade_minor_version">
<code class="sig-name descname">auto_upgrade_minor_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.auto_upgrade_minor_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The upgrade method to use. Valid values:</p>
<ul class="simple">
<li><p>Auto: Instances are automatically upgraded to a higher minor version.</p></li>
<li><p>Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>RDS database connection string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.db_instance_storage_type">
<code class="sig-name descname">db_instance_storage_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.db_instance_storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage type of the instance. Valid values:</p>
<ul class="simple">
<li><p>local_ssd: specifies to use local SSDs. This value is recommended.</p></li>
<li><p>cloud_ssd: specifies to use standard SSDs.</p></li>
<li><p>cloud_essd: specifies to use enhanced SSDs (ESSDs).</p></li>
<li><p>cloud_essd2: specifies to use enhanced SSDs (ESSDs).</p></li>
<li><p>cloud_essd3: specifies to use enhanced SSDs (ESSDs).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.force_restart">
<code class="sig-name descname">force_restart</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.force_restart" title="Permalink to this definition">¶</a></dt>
<dd><p>Set it to true to make some parameter efficient when modifying them. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">Prepaid</span></code>, <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>. Currently, the resource only supports PostPaid to PrePaid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of DB instance. It a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.instance_storage">
<code class="sig-name descname">instance_storage</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.instance_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined DB instance storage space. Value range:</p>
<ul class="simple">
<li><p>[5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;</p></li>
<li><p>[20,1000] for MySQL 5.7 basic single node edition;</p></li>
<li><p>[10, 2000] for SQL Server 2008R2;</p></li>
<li><p>[20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified <code class="docutils literal notranslate"><span class="pre">instance_storage</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.maintain_time">
<code class="sig-name descname">maintain_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.maintain_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.monitoring_period">
<code class="sig-name descname">monitoring_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.monitoring_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>RDS database connection port.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from 1.69.0 and use <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.security_ip_mode">
<code class="sig-name descname">security_ip_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.security_ip_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">safety</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">normal</span></code>. support <code class="docutils literal notranslate"><span class="pre">safety</span></code> switch to high security access mode</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.security_ips">
<code class="sig-name descname">security_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.security_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.sql_collector_config_value">
<code class="sig-name descname">sql_collector_config_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.sql_collector_config_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The sql collector keep time of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">180</span></code>, <code class="docutils literal notranslate"><span class="pre">365</span></code>, <code class="docutils literal notranslate"><span class="pre">1095</span></code>, <code class="docutils literal notranslate"><span class="pre">1825</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.sql_collector_status">
<code class="sig-name descname">sql_collector_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.sql_collector_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The sql collector status of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.Instance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.Instance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_upgrade_minor_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_restart</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_ip_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_collector_config_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_collector_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:[1~12], Default to 1.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The upgrade method to use. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Auto</span><span class="p">:</span> <span class="n">Instances</span> <span class="n">are</span> <span class="n">automatically</span> <span class="n">upgraded</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">minor</span> <span class="n">version</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Manual</span><span class="p">:</span> <span class="n">Instances</span> <span class="n">are</span> <span class="n">forcibly</span> <span class="n">upgraded</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">minor</span> <span class="n">version</span> <span class="n">when</span> <span class="n">the</span> <span class="n">current</span> <span class="n">version</span> <span class="ow">is</span> <span class="n">unpublished</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RDS database connection string.</p></li>
<li><p><strong>db_instance_storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The storage type of the instance. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">local_ssd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">local</span> <span class="n">SSDs</span><span class="o">.</span> <span class="n">This</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">recommended</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">standard</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd2</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_essd3</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">to</span> <span class="n">use</span> <span class="n">enhanced</span> <span class="n">SSDs</span> <span class="p">(</span><span class="n">ESSDs</span><span class="p">)</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>force_restart</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set it to true to make some parameter efficient when modifying them. Default to false.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">Prepaid</span></code>, <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Postpaid</span></code>. Currently, the resource only supports PostPaid to PrePaid.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined DB instance storage space. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
<li><p><strong>monitoring_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a> .</p>
</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RDS database connection port.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from 1.69.0 and use <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> instead.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – , Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.</p></li>
<li><p><strong>security_ip_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">safety</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">normal</span></code>. support <code class="docutils literal notranslate"><span class="pre">safety</span></code> switch to high security access mode</p></li>
<li><p><strong>security_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>sql_collector_config_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The sql collector keep time of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">180</span></code>, <code class="docutils literal notranslate"><span class="pre">365</span></code>, <code class="docutils literal notranslate"><span class="pre">1095</span></code>, <code class="docutils literal notranslate"><span class="pre">1825</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>sql_collector_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sql collector status of the instance. Valid values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.ReadOnlyInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">ReadOnlyInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_db_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS readonly instance resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</p></li>
<li><p><strong>master_db_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the master instance.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a>.</p>
</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>RDS database connection string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.engine">
<code class="sig-name descname">engine</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.engine" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of DB instance. It a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.instance_storage">
<code class="sig-name descname">instance_storage</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.instance_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.master_db_instance_id">
<code class="sig-name descname">master_db_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.master_db_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the master instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>RDS database connection port.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_db_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReadOnlyInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RDS database connection string.</p></li>
<li><p><strong>engine</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>DB Instance type. For details, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26312.htm">Instance type table</a>.</p>
</p></li>
<li><p><strong>master_db_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the master instance.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26284.htm">View database parameter templates</a>.</p>
</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RDS database connection port.</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.ReadOnlyInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadOnlyInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">ReadWriteSplittingConnection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">distribution_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an RDS read write splitting connection resource to allocate an Intranet connection string for RDS instance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘rw’.</p></li>
<li><p><strong>distribution_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read weight distribution mode. Values are as follows: <code class="docutils literal notranslate"><span class="pre">Standard</span></code> indicates automatic weight distribution based on types, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> indicates custom weight distribution.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>max_delay_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Delay threshold, in seconds. The value range is 0 to 7200. Default to 30. Read requests are not routed to the read-only instances with a delay greater than the threshold.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Intranet connection port. Valid value: [3001-3999]. Default to 3306.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Read weight distribution. Read weights increase at a step of 100 up to 10,000. Enter weights in the following format: {“Instanceid”:”Weight”,”Instanceid”:”Weight”}. This parameter must be set when distribution_type is set to Custom.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.connection_prefix">
<code class="sig-name descname">connection_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.connection_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘rw’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.connection_string">
<code class="sig-name descname">connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection instance string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.distribution_type">
<code class="sig-name descname">distribution_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.distribution_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Read weight distribution mode. Values are as follows: <code class="docutils literal notranslate"><span class="pre">Standard</span></code> indicates automatic weight distribution based on types, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> indicates custom weight distribution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance that can run database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.max_delay_time">
<code class="sig-name descname">max_delay_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.max_delay_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Delay threshold, in seconds. The value range is 0 to 7200. Default to 30. Read requests are not routed to the read-only instances with a delay greater than the threshold.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Intranet connection port. Valid value: [3001-3999]. Default to 3306.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Read weight distribution. Read weights increase at a step of 100 up to 10,000. Enter weights in the following format: {“Instanceid”:”Weight”,”Instanceid”:”Weight”}. This parameter must be set when distribution_type is set to Custom.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">distribution_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReadWriteSplittingConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘rw’.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection instance string.</p></li>
<li><p><strong>distribution_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read weight distribution mode. Values are as follows: <code class="docutils literal notranslate"><span class="pre">Standard</span></code> indicates automatic weight distribution based on types, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> indicates custom weight distribution.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>max_delay_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Delay threshold, in seconds. The value range is 0 to 7200. Default to 30. Read requests are not routed to the read-only instances with a delay greater than the threshold.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Intranet connection port. Valid value: [3001-3999]. Default to 3306.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Read weight distribution. Read weights increase at a step of 100 up to 10,000. Enter weights in the following format: {“Instanceid”:”Weight”,”Instanceid”:”Weight”}. This parameter must be set when distribution_type is set to Custom.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.ReadWriteSplittingConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.ReadWriteSplittingConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rds.get_instance_classes">
<code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">get_instance_classes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.get_instance_classes" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the RDS instance classes resource available info of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.46.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>category</strong> (<em>str</em>) – DB Instance category. the value like [<code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">HighAvailability</span></code>, <code class="docutils literal notranslate"><span class="pre">Finance</span></code>], <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/69795.htm">detail info</a>.</p></li>
<li><p><strong>db_instance_class</strong> (<em>str</em>) – The DB instance class type by the user.</p></li>
<li><p><strong>engine</strong> (<em>str</em>) – Database type. Options are <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code> and <code class="docutils literal notranslate"><span class="pre">PPAS</span></code>. If no value is specified, all types are returned.</p></li>
<li><p><strong>engine_version</strong> (<em>str</em>) – <p>Database version required by the user. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">detail info</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>multi_zone</strong> (<em>bool</em>) – Whether to show multi available zone. Default false to not show multi availability zone.</p></li>
<li><p><strong>storage_type</strong> (<em>str</em>) – The DB instance storage space required by the user. Valid values: <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">local_ssd</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Zone to launch the DB instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.rds.get_instance_engines">
<code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">get_instance_engines</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.get_instance_engines" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the RDS instance engines resource available info of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.46.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>engine</strong> (<em>str</em>) – Database type. Options are <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code> and <code class="docutils literal notranslate"><span class="pre">PPAS</span></code>. If no value is specified, all types are returned.</p></li>
<li><p><strong>engine_version</strong> (<em>str</em>) – <p>Database version required by the user. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/26228.htm">detail info</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>multi_zone</strong> (<em>bool</em>) – Whether to show multi available zone. Default false to not show multi availability zone.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Zone to launch the DB instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.rds.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">rds.getInstances</span></code> data source provides a collection of RDS instances available in Alibaba Cloud account.
Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connection_mode</strong> (<em>str</em>) – <code class="docutils literal notranslate"><span class="pre">Standard</span></code> for standard access mode and <code class="docutils literal notranslate"><span class="pre">Safe</span></code> for high security access mode.</p></li>
<li><p><strong>db_type</strong> (<em>str</em>) – <code class="docutils literal notranslate"><span class="pre">Primary</span></code> for primary instance, <code class="docutils literal notranslate"><span class="pre">Readonly</span></code> for read-only instance, <code class="docutils literal notranslate"><span class="pre">Guard</span></code> for disaster recovery instance, and <code class="docutils literal notranslate"><span class="pre">Temp</span></code> for temporary instance.</p></li>
<li><p><strong>engine</strong> (<em>str</em>) – Database type. Options are <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code> and <code class="docutils literal notranslate"><span class="pre">PPAS</span></code>. If no value is specified, all types are returned.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of RDS instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by instance name.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Status of the instance.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the DB instances. 
Note: Before 1.60.0, the value’s format is a <code class="docutils literal notranslate"><span class="pre">json</span></code> string which including <code class="docutils literal notranslate"><span class="pre">TagKey</span></code> and <code class="docutils literal notranslate"><span class="pre">TagValue</span></code>. <code class="docutils literal notranslate"><span class="pre">TagKey</span></code> cannot be null, and <code class="docutils literal notranslate"><span class="pre">TagValue</span></code> can be empty. Format example <code class="docutils literal notranslate"><span class="pre">&quot;{&quot;key1&quot;:&quot;value1&quot;}&quot;</span></code></p></li>
<li><p><strong>vpc_id</strong> (<em>str</em>) – Used to retrieve instances belong to specified VPC.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – Used to retrieve instances belong to specified <code class="docutils literal notranslate"><span class="pre">vswitch</span></code> resources.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.rds.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.rds.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rds.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for RDS that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.73.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by a specific instance charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch RDS instances.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
