<div class="section" id="module-pulumi_aws.glacier">
<span id="glacier"></span><h1>glacier<a class="headerlink" href="#module-pulumi_aws.glacier" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.glacier.Vault">
<em class="property">class </em><code class="descclassname">pulumi_aws.glacier.</code><code class="descname">Vault</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>access_policy=None</em>, <em>name=None</em>, <em>notifications=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Glacier Vault Resource. You can refer to the [Glacier Developer Guide](<a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html">https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html</a>) for a full explanation of the Glacier Vault functionality</p>
<p>&gt; <strong>NOTE:</strong> When removing a Glacier Vault, the Vault must be empty.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>access_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string.
The heredoc syntax or <cite>file</cite> function is helpful here. Use the [Glacier Developer Guide](<a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html</a>) for more information on Glacier Vault Policy</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘_’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</li>
<li><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notifications for the Vault. Fields documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.access_policy">
<code class="descname">access_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.
The heredoc syntax or <cite>file</cite> function is helpful here. Use the [Glacier Developer Guide](<a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html">https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html</a>) for more information on Glacier Vault Policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the vault that was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, ‘_’ (underscore), ‘-‘ (hyphen), and ‘.’ (period).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.notifications">
<code class="descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The notifications for the Vault. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.Vault.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.Vault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.Vault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.glacier.VaultLock">
<em class="property">class </em><code class="descclassname">pulumi_aws.glacier.</code><code class="descname">VaultLock</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>complete_lock=None</em>, <em>ignore_deletion_error=None</em>, <em>policy=None</em>, <em>vault_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Glacier Vault Lock. You can refer to the [Glacier Developer Guide](<a class="reference external" href="https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html">https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html</a>) for a full explanation of the Glacier Vault Lock functionality.</p>
<p>&gt; <strong>NOTE:</strong> This resource allows you to test Glacier Vault Lock policies by setting the <cite>complete_lock</cite> argument to <cite>false</cite>. When testing policies in this manner, the Glacier Vault Lock automatically expires after 24 hours and Terraform will show this resource as needing recreation after that time. To permanently apply the policy, set the <cite>complete_lock</cite> argument to <cite>true</cite>. When changing <cite>complete_lock</cite> to <cite>true</cite>, it is expected the resource will show as recreating.</p>
<p>!&gt; <strong>WARNING:</strong> Once a Glacier Vault Lock is completed, it is immutable. The deletion of the Glacier Vault Lock is not be possible and attempting to remove it from Terraform will return an error. Set the <cite>ignore_deletion_error</cite> argument to <cite>true</cite> and apply this configuration before attempting to delete this resource via Terraform or use <cite>terraform state rm</cite> to remove this resource from Terraform management.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>complete_lock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to <cite>false</cite>, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the Terraform resource will show as needing recreation. Changing this from <cite>false</cite> to <cite>true</cite> will show as resource recreation, which is expected. Changing this from <cite>true</cite> to <cite>false</cite> is not possible unless the Glacier Vault is recreated at the same time.</li>
<li><strong>ignore_deletion_error</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow Terraform to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via Terraform, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with <cite>complete_lock</cite> being set to <cite>true</cite>.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</li>
<li><strong>vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Glacier Vault.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.complete_lock">
<code class="descname">complete_lock</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.complete_lock" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to <cite>false</cite>, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the Terraform resource will show as needing recreation. Changing this from <cite>false</cite> to <cite>true</cite> will show as resource recreation, which is expected. Changing this from <cite>true</cite> to <cite>false</cite> is not possible unless the Glacier Vault is recreated at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.ignore_deletion_error">
<code class="descname">ignore_deletion_error</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.ignore_deletion_error" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow Terraform to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via Terraform, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with <cite>complete_lock</cite> being set to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.glacier.VaultLock.vault_name">
<code class="descname">vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Glacier Vault.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.VaultLock.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.glacier.VaultLock.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.glacier.VaultLock.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
