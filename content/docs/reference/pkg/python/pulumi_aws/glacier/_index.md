---
title: Module glacier
title_tag: Module glacier | Package pulumi_aws | Python SDK
linktitle: glacier
notitle: true
---

<div class="section" id="glacier">
<h1>glacier<a class="headerlink" href="#glacier" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.glacier"></span><dl class="py class">
<dt id="pulumi_aws.glacier.Vault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glacier.</code><code class="sig-name descname">Vault</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glacier Vault Resource. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html">Glacier Developer Guide</a> for a full explanation of the Glacier Vault functionality</p>
<blockquote>
<div><p><strong>NOTE:</strong> When removing a Glacier Vault, the Vault must be empty.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access*policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy document. This is a JSON formatted string.
The heredoc syntax or <code class="docutils literal notranslate"><span class="pre">file</span></code> function is helpful here. Use the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">Glacier Developer Guide</a> for more information on Glacier Vault Policy</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘<a href="#id4"><span class="problematic" id="id5">*</span></a>’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notifications for the Vault. Fields documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - You can configure a vault to publish a notification for <code class="docutils literal notranslate"><span class="pre">ArchiveRetrievalCompleted</span></code> and <code class="docutils literal notranslate"><span class="pre">InventoryRetrievalCompleted</span></code> events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sns_topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SNS Topic ARN.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.access_policy">
<code class="sig-name descname">access_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.
The heredoc syntax or <code class="docutils literal notranslate"><span class="pre">file</span></code> function is helpful here. Use the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">Glacier Developer Guide</a> for more information on Glacier Vault Policy</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the vault.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the vault that was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘_’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.notifications">
<code class="sig-name descname">notifications</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The notifications for the Vault. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - You can configure a vault to publish a notification for <code class="docutils literal notranslate"><span class="pre">ArchiveRetrievalCompleted</span></code> and <code class="docutils literal notranslate"><span class="pre">InventoryRetrievalCompleted</span></code> events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sns_topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SNS Topic ARN.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.Vault.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glacier.Vault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access*policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy document. This is a JSON formatted string.
The heredoc syntax or <code class="docutils literal notranslate"><span class="pre">file</span></code> function is helpful here. Use the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">Glacier Developer Guide</a> for more information on Glacier Vault Policy</p>
</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the vault.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the vault that was created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘<a href="#id10"><span class="problematic" id="id11">*</span></a>’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notifications for the Vault. Fields documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - You can configure a vault to publish a notification for <code class="docutils literal notranslate"><span class="pre">ArchiveRetrievalCompleted</span></code> and <code class="docutils literal notranslate"><span class="pre">InventoryRetrievalCompleted</span></code> events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sns_topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SNS Topic ARN.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glacier.Vault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.Vault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.VaultLock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.glacier.</code><code class="sig-name descname">VaultLock</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">complete_lock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_deletion_error</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vault_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glacier Vault Lock. You can refer to the <a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html">Glacier Developer Guide</a> for a full explanation of the Glacier Vault Lock functionality.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource allows you to test Glacier Vault Lock policies by setting the <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> argument to <code class="docutils literal notranslate"><span class="pre">false</span></code>. When testing policies in this manner, the Glacier Vault Lock automatically expires after 24 hours and this provider will show this resource as needing recreation after that time. To permanently apply the policy, set the <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> argument to <code class="docutils literal notranslate"><span class="pre">true</span></code>. When changing <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>, it is expected the resource will show as recreating.</p>
</div></blockquote>
<p>!&gt; <strong>WARNING:</strong> Once a Glacier Vault Lock is completed, it is immutable. The deletion of the Glacier Vault Lock is not be possible and attempting to remove it from this provider will return an error. Set the <code class="docutils literal notranslate"><span class="pre">ignore_deletion_error</span></code> argument to <code class="docutils literal notranslate"><span class="pre">true</span></code> and apply this configuration before attempting to delete this resource via this provider or remove this resource from this provider’s management.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>complete_lock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from <code class="docutils literal notranslate"><span class="pre">false</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code> will show as resource recreation, which is expected. Changing this from <code class="docutils literal notranslate"><span class="pre">true</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code> is not possible unless the Glacier Vault is recreated at the same time.</p></li>
<li><p><strong>ignore_deletion_error</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> being set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</p></li>
<li><p><strong>vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glacier Vault.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.glacier.VaultLock.complete_lock">
<code class="sig-name descname">complete_lock</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.complete_lock" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from <code class="docutils literal notranslate"><span class="pre">false</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code> will show as resource recreation, which is expected. Changing this from <code class="docutils literal notranslate"><span class="pre">true</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code> is not possible unless the Glacier Vault is recreated at the same time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.VaultLock.ignore_deletion_error">
<code class="sig-name descname">ignore_deletion_error</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.ignore_deletion_error" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> being set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.VaultLock.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.glacier.VaultLock.vault_name">
<code class="sig-name descname">vault_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Glacier Vault.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glacier.VaultLock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">complete_lock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_deletion_error</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vault_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VaultLock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>complete_lock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from <code class="docutils literal notranslate"><span class="pre">false</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code> will show as resource recreation, which is expected. Changing this from <code class="docutils literal notranslate"><span class="pre">true</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code> is not possible unless the Glacier Vault is recreated at the same time.</p></li>
<li><p><strong>ignore_deletion_error</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with <code class="docutils literal notranslate"><span class="pre">complete_lock</span></code> being set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</p></li>
<li><p><strong>vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glacier Vault.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.glacier.VaultLock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.glacier.VaultLock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
