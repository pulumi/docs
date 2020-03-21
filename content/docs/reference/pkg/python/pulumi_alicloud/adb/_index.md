---
title: Module adb
title_tag: Module adb | Package pulumi_alicloud | Python SDK
linktitle: adb
notitle: true
---

<div class="section" id="adb">
<h1>adb<a class="headerlink" href="#adb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.adb"></span><dl class="class">
<dt id="pulumi_alicloud.adb.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_description=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a <a class="reference external" href="https://www.alibabacloud.com/help/product/92664.htm">ADB</a> account resource and used to manage databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.71.0+.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_account.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id4"><span class="problematic" id="id5">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.account_description">
<code class="sig-name descname">account_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.account_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.account_password">
<code class="sig-name descname">account_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.account_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster in which account belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Account.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Account.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_description=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Account description. It cannot begin with <a class="reference external" href="https://">https://</a>. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (<a href="#id9"><span class="problematic" id="id10">*</span></a>), hyphens (-), and numbers. The length may be 2-256 characters.</p>
</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</p></li>
<li><p><strong>db_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of cluster in which account belongs.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.adb.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.adb.BackupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">BackupPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">preferred_backup_periods=None</em>, <em class="sig-param">preferred_backup_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BackupPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] db_cluster_id: The Id of cluster that can run database.
:param pulumi.Input[list] preferred_backup_periods: ADB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].
:param pulumi.Input[str] preferred_backup_time: ADB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.adb.BackupPolicy.backup_retention_period">
<code class="sig-name descname">backup_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.backup_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster backup retention days, Fixed for 7 days, not modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.BackupPolicy.db_cluster_id">
<code class="sig-name descname">db_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.db_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of cluster that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.BackupPolicy.preferred_backup_periods">
<code class="sig-name descname">preferred_backup_periods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.preferred_backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>ADB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.BackupPolicy.preferred_backup_time">
<code class="sig-name descname">preferred_backup_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.preferred_backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>ADB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.BackupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_retention_period=None</em>, <em class="sig-param">db_cluster_id=None</em>, <em class="sig-param">preferred_backup_periods=None</em>, <em class="sig-param">preferred_backup_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>preferred_backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ADB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [“Tuesday”, “Thursday”, “Saturday”].</p></li>
<li><p><strong>preferred_backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ADB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to “02:00Z-03:00Z”. China time is 8 hours behind it.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.BackupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.BackupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.BackupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_renew_period=None</em>, <em class="sig-param">db_cluster_category=None</em>, <em class="sig-param">db_cluster_version=None</em>, <em class="sig-param">db_node_class=None</em>, <em class="sig-param">db_node_count=None</em>, <em class="sig-param">db_node_storage=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">maintain_time=None</em>, <em class="sig-param">pay_type=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewal_status=None</em>, <em class="sig-param">security_ips=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a ADB cluster resource. A ADB cluster is an isolated database
environment in the cloud. A ADB cluster can contain multiple user-created
databases.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.71.0+.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p></li>
<li><p><strong>db_cluster_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster category. Value options: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>.</p></li>
<li><p><strong>db_cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster version. Value options: <code class="docutils literal notranslate"><span class="pre">3.0</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">3.0</span></code>.</p></li>
<li><p><strong>db_node_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db_node_class of cluster node.</p></li>
<li><p><strong>db_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The db_node_count of cluster node.</p></li>
<li><p><strong>db_node_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The db_node_storage of cluster node.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of cluster.</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB cluster.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.db_cluster_category">
<code class="sig-name descname">db_cluster_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.db_cluster_category" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster category. Value options: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.db_cluster_version">
<code class="sig-name descname">db_cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.db_cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster version. Value options: <code class="docutils literal notranslate"><span class="pre">3.0</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">3.0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.db_node_class">
<code class="sig-name descname">db_node_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.db_node_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The db_node_class of cluster node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.db_node_count">
<code class="sig-name descname">db_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.db_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The db_node_count of cluster node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.db_node_storage">
<code class="sig-name descname">db_node_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.db_node_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>The db_node_storage of cluster node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.maintain_time">
<code class="sig-name descname">maintain_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.maintain_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.pay_type">
<code class="sig-name descname">pay_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Currently, the resource can not supports change pay type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy DB cluster (in month). It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.renewal_status">
<code class="sig-name descname">renewal_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.renewal_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">AutoRenewal</span></code>, <code class="docutils literal notranslate"><span class="pre">Normal</span></code>, <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.security_ips">
<code class="sig-name descname">security_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.security_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.Cluster.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_renew_period=None</em>, <em class="sig-param">db_cluster_category=None</em>, <em class="sig-param">db_cluster_version=None</em>, <em class="sig-param">db_node_class=None</em>, <em class="sig-param">db_node_count=None</em>, <em class="sig-param">db_node_storage=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">maintain_time=None</em>, <em class="sig-param">pay_type=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewal_status=None</em>, <em class="sig-param">security_ips=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.</p></li>
<li><p><strong>db_cluster_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster category. Value options: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>.</p></li>
<li><p><strong>db_cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster version. Value options: <code class="docutils literal notranslate"><span class="pre">3.0</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">3.0</span></code>.</p></li>
<li><p><strong>db_node_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db_node_class of cluster node.</p></li>
<li><p><strong>db_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The db_node_count of cluster node.</p></li>
<li><p><strong>db_node_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The db_node_storage of cluster node.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of cluster.</p></li>
<li><p><strong>maintain_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)</p></li>
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
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.adb.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.adb.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">clusters=None</em>, <em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ADB clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetClustersResult.descriptions">
<code class="sig-name descname">descriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetClustersResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ADB cluster descriptions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ADB cluster IDs.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.adb.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.adb.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.adb.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.adb.get_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">adb.getClusters</span></code> data source provides a collection of ADB clusters available in Alibaba Cloud account.
Filters support regular expression for the cluster description, searches by tags, and other filters which are listed below.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.71.0+.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/adb_clusters.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/adb_clusters.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter results by cluster description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of ADB cluster IDs.</p></li>
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
<dt id="pulumi_alicloud.adb.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.adb.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.adb.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for ADB that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.73.0+.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/adb_zones.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/adb_zones.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch ADB instances.</p>
</dd>
</dl>
</dd></dl>

</div>
