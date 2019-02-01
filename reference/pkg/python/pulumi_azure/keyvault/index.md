<div class="section" id="module-pulumi_azure.keyvault">
<span id="keyvault"></span><h1>keyvault<a class="headerlink" href="#module-pulumi_azure.keyvault" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.keyvault.AccessPolicy">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">AccessPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>application_id=None</em>, <em>certificate_permissions=None</em>, <em>key_permissions=None</em>, <em>object_id=None</em>, <em>resource_group_name=None</em>, <em>secret_permissions=None</em>, <em>tenant_id=None</em>, <em>vault_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Access Policy.</p>
<p>&gt; <strong>NOTE:</strong> It’s possible to define Key Vault Access Policies both within the <cite>azurerm_key_vault</cite> resource via the <cite>access_policy</cite> block and by using the <cite>azurerm_key_vault_access_policy</cite> resource. However it’s not possible to use both methods to manage Access Policies within a KeyVault, since there’ll be conflicts.</p>
<p>-&gt; <strong>NOTE:</strong> Azure permits a maximum of 16 Access Policies per Key Vault - [more information can be found in this document](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control">https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of an Application in Azure Active Directory.</li>
<li><strong>certificate_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of certificate permissions, must be one or more from
the following: <cite>create</cite>, <cite>delete</cite>, <cite>deleteissuers</cite>, <cite>get</cite>, <cite>getissuers</cite>, <cite>import</cite>, <cite>list</cite>, <cite>listissuers</cite>,
<cite>managecontacts</cite>, <cite>manageissuers</cite>, <cite>purge</cite>, <cite>recover</cite>, <cite>setissuers</cite> and <cite>update</cite>.</li>
<li><strong>key_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of key permissions, must be one or more from
the following: <cite>backup</cite>, <cite>create</cite>, <cite>decrypt</cite>, <cite>delete</cite>, <cite>encrypt</cite>, <cite>get</cite>, <cite>import</cite>, <cite>list</cite>, <cite>purge</cite>,
<cite>recover</cite>, <cite>restore</cite>, <cite>sign</cite>, <cite>unwrapKey</cite>, <cite>update</cite>, <cite>verify</cite> and <cite>wrapKey</cite>.</li>
<li><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</li>
<li><strong>secret_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of secret permissions, must be one or more
from the following: <cite>backup</cite>, <cite>delete</cite>, <cite>get</cite>, <cite>list</cite>, <cite>purge</cite>, <cite>recover</cite>, <cite>restore</cite> and <cite>set</cite>.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.</li>
<li><strong>vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault resource. Changing this
forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The object ID of an Application in Azure Active Directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.certificate_permissions">
<code class="descname">certificate_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.certificate_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of certificate permissions, must be one or more from
the following: <cite>create</cite>, <cite>delete</cite>, <cite>deleteissuers</cite>, <cite>get</cite>, <cite>getissuers</cite>, <cite>import</cite>, <cite>list</cite>, <cite>listissuers</cite>,
<cite>managecontacts</cite>, <cite>manageissuers</cite>, <cite>purge</cite>, <cite>recover</cite>, <cite>setissuers</cite> and <cite>update</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.key_permissions">
<code class="descname">key_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.key_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of key permissions, must be one or more from
the following: <cite>backup</cite>, <cite>create</cite>, <cite>decrypt</cite>, <cite>delete</cite>, <cite>encrypt</cite>, <cite>get</cite>, <cite>import</cite>, <cite>list</cite>, <cite>purge</cite>,
<cite>recover</cite>, <cite>restore</cite>, <cite>sign</cite>, <cite>unwrapKey</cite>, <cite>update</cite>, <cite>verify</cite> and <cite>wrapKey</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.secret_permissions">
<code class="descname">secret_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.secret_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of secret permissions, must be one or more
from the following: <cite>backup</cite>, <cite>delete</cite>, <cite>get</cite>, <cite>list</cite>, <cite>purge</cite>, <cite>recover</cite>, <cite>restore</cite> and <cite>set</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.vault_name">
<code class="descname">vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault resource. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.AccessPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.AccessPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Certifiate">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">Certifiate</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate=None</em>, <em>certificate_policy=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Certificate.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>certificate</cite> block as defined below, used to Import an existing certificate.</li>
<li><strong>certificate_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>certificate_policy</cite> block as defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Certificate Issuer. Possible values include <cite>Self</cite>, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vault_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>certificate</cite> block as defined below, used to Import an existing certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate_data">
<code class="descname">certificate_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw Key Vault Certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate_policy">
<code class="descname">certificate_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>certificate_policy</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Certificate Issuer. Possible values include <cite>Self</cite>, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.secret_id">
<code class="descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.thumbprint">
<code class="descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The X509 Thumbprint of the Key Vault Certificate returned as hex string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.vault_uri">
<code class="descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Certifiate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Certifiate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">GetAccessPolicyResult</code><span class="sig-paren">(</span><em>certificate_permissions=None</em>, <em>key_permissions=None</em>, <em>secret_permissions=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.certificate_permissions">
<code class="descname">certificate_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.certificate_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the certificate permissions for the access policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.key_permissions">
<code class="descname">key_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.key_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the key permissions for the access policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.secret_permissions">
<code class="descname">secret_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.secret_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the secret permissions for the access policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">GetKeyResult</code><span class="sig-paren">(</span><em>e=None</em>, <em>key_opts=None</em>, <em>key_size=None</em>, <em>key_type=None</em>, <em>n=None</em>, <em>tags=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.e">
<code class="descname">e</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.e" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA public exponent of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_opts">
<code class="descname">key_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of JSON web key operations assigned to this Key Vault Key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_size">
<code class="descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Size of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_type">
<code class="descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Key Type of this Key Vault Key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.n">
<code class="descname">n</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.n" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA modulus of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">GetKeyVaultResult</code><span class="sig-paren">(</span><em>access_policies=None</em>, <em>enabled_for_deployment=None</em>, <em>enabled_for_disk_encryption=None</em>, <em>enabled_for_template_deployment=None</em>, <em>location=None</em>, <em>network_acls=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>vault_uri=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyVault.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.access_policies">
<code class="descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>access_policy</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_deployment">
<code class="descname">enabled_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Virtual Machines retrieve certificates stored as secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_disk_encryption">
<code class="descname">enabled_for_disk_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_disk_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Disk Encryption retrieve secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_template_deployment">
<code class="descname">enabled_for_template_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_template_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Resource Manager retrieve secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Key Vault exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Key Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory Tenant ID used to authenticate requests for this Key Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.vault_uri">
<code class="descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the vault for performing operations on keys and secrets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetSecretResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">GetSecretResult</code><span class="sig-paren">(</span><em>content_type=None</em>, <em>tags=None</em>, <em>value=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type for the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Any tags assigned to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.Key">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">Key</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>key_opts=None</em>, <em>key_size=None</em>, <em>key_type=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key_opts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of JSON web key operations. Possible values include: <cite>decrypt</cite>, <cite>encrypt</cite>, <cite>sign</cite>, <cite>unwrapKey</cite>, <cite>verify</cite> and <cite>wrapKey</cite>. Please note these values are case sensitive.</li>
<li><strong>key_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.</li>
<li><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Key Type to use for this Key Vault Key. Possible values are <cite>EC</cite> (Elliptic Curve), <cite>Oct</cite> (Octet), <cite>RSA</cite> and <cite>RSA-HSM</cite>. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vault_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.e">
<code class="descname">e</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.e" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA public exponent of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_opts">
<code class="descname">key_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of JSON web key operations. Possible values include: <cite>decrypt</cite>, <cite>encrypt</cite>, <cite>sign</cite>, <cite>unwrapKey</cite>, <cite>verify</cite> and <cite>wrapKey</cite>. Please note these values are case sensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_size">
<code class="descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_type">
<code class="descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Key Type to use for this Key Vault Key. Possible values are <cite>EC</cite> (Elliptic Curve), <cite>Oct</cite> (Octet), <cite>RSA</cite> and <cite>RSA-HSM</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.n">
<code class="descname">n</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.n" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA modulus of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.vault_uri">
<code class="descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Key.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Key.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.KeyVault">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">KeyVault</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>access_policies=None</em>, <em>enabled_for_deployment=None</em>, <em>enabled_for_disk_encryption=None</em>, <em>enabled_for_template_deployment=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_acls=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault.</p>
<p>&gt; <strong>NOTE:</strong> It’s possible to define Key Vault Access Policies both within the <cite>azurerm_key_vault</cite> resource via the <cite>access_policy</cite> block and by using the <cite>azurerm_key_vault_access_policy</cite> resource. However it’s not possible to use both methods to manage Access Policies within a KeyVault, since there’ll be conflicts.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An access policy block as described below. A maximum of 16 may be declared.</li>
<li><strong>enabled_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to <cite>false</cite>.</li>
<li><strong>enabled_for_disk_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to <cite>false</cite>.</li>
<li><strong>enabled_for_template_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to <cite>false</cite>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault. Changing this forces a new resource to be created.</li>
<li><strong>network_acls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>network_acls</cite> block as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An SKU block as described below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.access_policies">
<code class="descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An access policy block as described below. A maximum of 16 may be declared.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_deployment">
<code class="descname">enabled_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_disk_encryption">
<code class="descname">enabled_for_disk_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_disk_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_template_deployment">
<code class="descname">enabled_for_template_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_template_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.network_acls">
<code class="descname">network_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.network_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>network_acls</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>An SKU block as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.vault_uri">
<code class="descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Key Vault, used for performing operations on keys and secrets.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.KeyVault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.KeyVault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Secret">
<em class="property">class </em><code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">Secret</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content_type=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>value=None</em>, <em>vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Secret.</p>
<p>&gt; <strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the content type for the Key Vault Secret.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the Key Vault Secret.</li>
<li><strong>vault_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the content type for the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.vault_uri">
<code class="descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI used to access the Key Vault instance, available on the <cite>azurerm_key_vault</cite> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Secret.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Secret.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Secret.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.get_access_policy">
<code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">get_access_policy</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the permissions from the Management Key Vault Templates.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_key">
<code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">get_key</code><span class="sig-paren">(</span><em>name=None</em>, <em>vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault Key.</p>
<p>&gt; <strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_key_vault">
<code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">get_key_vault</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_key_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_secret">
<code class="descclassname">pulumi_azure.keyvault.</code><code class="descname">get_secret</code><span class="sig-paren">(</span><em>name=None</em>, <em>vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault Secret.</p>
<p>&gt; <strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
</dd></dl>

</div>
