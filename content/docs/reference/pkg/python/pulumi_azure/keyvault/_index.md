---
title: Module keyvault
title_tag: Module keyvault | Package pulumi_azure | Python SDK
linktitle: keyvault
notitle: true
---

<div class="section" id="keyvault">
<h1>keyvault<a class="headerlink" href="#keyvault" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.keyvault"></span><dl class="class">
<dt id="pulumi_azure.keyvault.AccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">AccessPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">certificate_permissions=None</em>, <em class="sig-param">key_permissions=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">secret_permissions=None</em>, <em class="sig-param">storage_permissions=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Access Policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> It’s possible to define Key Vault Access Policies both within the <code class="docutils literal notranslate"><span class="pre">keyvault.KeyVault</span></code> resource via the <code class="docutils literal notranslate"><span class="pre">access_policy</span></code> block and by using the <code class="docutils literal notranslate"><span class="pre">keyvault.AccessPolicy</span></code> resource. However it’s not possible to use both methods to manage Access Policies within a KeyVault, since there’ll be conflicts.</p>
<p><strong>NOTE:</strong> Azure permits a maximum of 1024 Access Policies per Key Vault - <a class="reference external" href="https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control">more information can be found in this document</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of an Application in Azure Active Directory.</p></li>
<li><p><strong>certificate_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of certificate permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deleteissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listissuers</span></code>,
<code class="docutils literal notranslate"><span class="pre">managecontacts</span></code>, <code class="docutils literal notranslate"><span class="pre">manageissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">setissuers</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p></li>
<li><p><strong>key_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of key permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>,
<code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">update</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the Key Vault resource. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.</p></li>
<li><p><strong>secret_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of secret permissions, must be one or more
from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code> and <code class="docutils literal notranslate"><span class="pre">set</span></code>.</p></li>
<li><p><strong>storage_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of storage permissions, must be one or more from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deletesas</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getsas</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listsas</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">regeneratekey</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">set</span></code>, <code class="docutils literal notranslate"><span class="pre">setsas</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The object ID of an Application in Azure Active Directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.certificate_permissions">
<code class="sig-name descname">certificate_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.certificate_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of certificate permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deleteissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listissuers</span></code>,
<code class="docutils literal notranslate"><span class="pre">managecontacts</span></code>, <code class="docutils literal notranslate"><span class="pre">manageissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">setissuers</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.key_permissions">
<code class="sig-name descname">key_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.key_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of key permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>,
<code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">update</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the Key Vault resource. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.secret_permissions">
<code class="sig-name descname">secret_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.secret_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of secret permissions, must be one or more
from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code> and <code class="docutils literal notranslate"><span class="pre">set</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.storage_permissions">
<code class="sig-name descname">storage_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.storage_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of storage permissions, must be one or more from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deletesas</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getsas</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listsas</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">regeneratekey</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">set</span></code>, <code class="docutils literal notranslate"><span class="pre">setsas</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.AccessPolicy.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.AccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">certificate_permissions=None</em>, <em class="sig-param">key_permissions=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">secret_permissions=None</em>, <em class="sig-param">storage_permissions=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of an Application in Azure Active Directory.</p></li>
<li><p><strong>certificate_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of certificate permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deleteissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listissuers</span></code>,
<code class="docutils literal notranslate"><span class="pre">managecontacts</span></code>, <code class="docutils literal notranslate"><span class="pre">manageissuers</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">setissuers</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p></li>
<li><p><strong>key_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of key permissions, must be one or more from
the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">create</span></code>, <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">import</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>,
<code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">update</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the Key Vault resource. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.</p></li>
<li><p><strong>secret_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of secret permissions, must be one or more
from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code> and <code class="docutils literal notranslate"><span class="pre">set</span></code>.</p></li>
<li><p><strong>storage_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of storage permissions, must be one or more from the following: <code class="docutils literal notranslate"><span class="pre">backup</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">deletesas</span></code>, <code class="docutils literal notranslate"><span class="pre">get</span></code>, <code class="docutils literal notranslate"><span class="pre">getsas</span></code>, <code class="docutils literal notranslate"><span class="pre">list</span></code>, <code class="docutils literal notranslate"><span class="pre">listsas</span></code>, <code class="docutils literal notranslate"><span class="pre">purge</span></code>, <code class="docutils literal notranslate"><span class="pre">recover</span></code>, <code class="docutils literal notranslate"><span class="pre">regeneratekey</span></code>, <code class="docutils literal notranslate"><span class="pre">restore</span></code>, <code class="docutils literal notranslate"><span class="pre">set</span></code>, <code class="docutils literal notranslate"><span class="pre">setsas</span></code> and <code class="docutils literal notranslate"><span class="pre">update</span></code>.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.AccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.AccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.AwaitableGetAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">AwaitableGetAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">certificate_permissions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_permissions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secret_permissions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AwaitableGetAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.AwaitableGetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">AwaitableGetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">e=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_opts=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">n=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AwaitableGetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.AwaitableGetKeyVaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">AwaitableGetKeyVaultResult</code><span class="sig-paren">(</span><em class="sig-param">access_policies=None</em>, <em class="sig-param">enabled_for_deployment=None</em>, <em class="sig-param">enabled_for_disk_encryption=None</em>, <em class="sig-param">enabled_for_template_deployment=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_acls=None</em>, <em class="sig-param">purge_protection_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">soft_delete_enabled=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AwaitableGetKeyVaultResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.AwaitableGetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">AwaitableGetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">content_type=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.AwaitableGetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.Certifiate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">Certifiate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_policy=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Certificate.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p></li>
<li><p><strong>certificate_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Certificate should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>certificate_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate_data">
<code class="sig-name descname">certificate_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw Key Vault Certificate data represented as a hexadecimal string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.certificate_policy">
<code class="sig-name descname">certificate_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.certificate_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key Vault where the Certificate should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.secret_id">
<code class="sig-name descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certifiate.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Certifiate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_data=None</em>, <em class="sig-param">certificate_policy=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secret_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certifiate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p></li>
<li><p><strong>certificate_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The raw Key Vault Certificate data represented as a hexadecimal string.</p></li>
<li><p><strong>certificate_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Certificate should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Key Vault Secret.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the Key Vault Certificate.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>certificate_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Certifiate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Certifiate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certifiate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_policy=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Certificate.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p></li>
<li><p><strong>certificate_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Certificate should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>certificate_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.certificate_data">
<code class="sig-name descname">certificate_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.certificate_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw Key Vault Certificate data represented as a hexadecimal string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.certificate_policy">
<code class="sig-name descname">certificate_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.certificate_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key Vault where the Certificate should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.secret_id">
<code class="sig-name descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Certificate.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_data=None</em>, <em class="sig-param">certificate_policy=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secret_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below, used to Import an existing certificate.</p></li>
<li><p><strong>certificate_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The raw Key Vault Certificate data represented as a hexadecimal string.</p></li>
<li><p><strong>certificate_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_policy</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Certificate should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Key Vault Secret.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the Key Vault Certificate.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base64-encoded certificate contents. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>certificate_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">issuerParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">issuer_parameters</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Issuer. Possible values include <code class="docutils literal notranslate"><span class="pre">Self</span></code> (for self-signed certificate), or <code class="docutils literal notranslate"><span class="pre">Unknown</span></code> (for a certificate issuing authority like <code class="docutils literal notranslate"><span class="pre">Let's</span> <span class="pre">Encrypt</span></code> and Azure direct supported ones). Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exportable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Certificate Exportable? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Key used in the Certificate. Possible values include <code class="docutils literal notranslate"><span class="pre">2048</span></code> and <code class="docutils literal notranslate"><span class="pre">4096</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Type of Key, such as <code class="docutils literal notranslate"><span class="pre">RSA</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reuseKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the key reusable? Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">lifetime_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of action to be performed when the lifetime trigger is triggerec. Possible values include <code class="docutils literal notranslate"><span class="pre">AutoRenew</span></code> and <code class="docutils literal notranslate"><span class="pre">EmailContacts</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysBeforeExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">lifetime_percentage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">days_before_expiry</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">secret_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content-Type of the Certificate, such as <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code> for a PFX or <code class="docutils literal notranslate"><span class="pre">application/x-pem-file</span></code> for a PEM. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509CertificateProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">x509_certificate_properties</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">extendedKeyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUsages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of uses associated with this Key. Possible values include <code class="docutils literal notranslate"><span class="pre">cRLSign</span></code>, <code class="docutils literal notranslate"><span class="pre">dataEncipherment</span></code>, <code class="docutils literal notranslate"><span class="pre">decipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">digitalSignature</span></code>, <code class="docutils literal notranslate"><span class="pre">encipherOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">keyAgreement</span></code>, <code class="docutils literal notranslate"><span class="pre">keyCertSign</span></code>, <code class="docutils literal notranslate"><span class="pre">keyEncipherment</span></code> and <code class="docutils literal notranslate"><span class="pre">nonRepudiation</span></code> and are case-sensitive. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Certificate’s Subject. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectAlternativeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">subject_alternative_names</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validityInMonths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Certificates Validity Period in Months. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">GetAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">certificate_permissions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_permissions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">secret_permissions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.certificate_permissions">
<code class="sig-name descname">certificate_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.certificate_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the certificate permissions for the access policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.key_permissions">
<code class="sig-name descname">key_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.key_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the key permissions for the access policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetAccessPolicyResult.secret_permissions">
<code class="sig-name descname">secret_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetAccessPolicyResult.secret_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the secret permissions for the access policy</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">GetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">e=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_opts=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">n=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.e">
<code class="sig-name descname">e</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.e" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA public exponent of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_opts">
<code class="sig-name descname">key_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of JSON web key operations assigned to this Key Vault Key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_size">
<code class="sig-name descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Size of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.key_type">
<code class="sig-name descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Key Type of this Key Vault Key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.n">
<code class="sig-name descname">n</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.n" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA modulus of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Key.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">GetKeyVaultResult</code><span class="sig-paren">(</span><em class="sig-param">access_policies=None</em>, <em class="sig-param">enabled_for_deployment=None</em>, <em class="sig-param">enabled_for_disk_encryption=None</em>, <em class="sig-param">enabled_for_template_deployment=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_acls=None</em>, <em class="sig-param">purge_protection_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">soft_delete_enabled=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyVault.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.access_policies">
<code class="sig-name descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">access_policy</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_deployment">
<code class="sig-name descname">enabled_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Virtual Machines retrieve certificates stored as secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_disk_encryption">
<code class="sig-name descname">enabled_for_disk_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_disk_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Disk Encryption retrieve secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_template_deployment">
<code class="sig-name descname">enabled_for_template_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.enabled_for_template_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Azure Resource Manager retrieve secrets from the Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Key Vault exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.purge_protection_enabled">
<code class="sig-name descname">purge_protection_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.purge_protection_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is purge protection enabled on this Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the SKU used for this Key Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.soft_delete_enabled">
<code class="sig-name descname">soft_delete_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.soft_delete_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is soft delete enabled on this Key Vault?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Key Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory Tenant ID used to authenticate requests for this Key Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetKeyVaultResult.vault_uri">
<code class="sig-name descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetKeyVaultResult.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the vault for performing operations on keys and secrets.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.GetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">GetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">content_type=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type for the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Any tags assigned to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.GetSecretResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.GetSecretResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Secret.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.keyvault.Key">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">Key</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">curve=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">key_opts=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_before_date=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Key.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_key.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the curve to use when creating an <code class="docutils literal notranslate"><span class="pre">EC</span></code> key. Possible values are <code class="docutils literal notranslate"><span class="pre">P-256</span></code>, <code class="docutils literal notranslate"><span class="pre">P-384</span></code>, <code class="docutils literal notranslate"><span class="pre">P-521</span></code>, and <code class="docutils literal notranslate"><span class="pre">SECP256K1</span></code>. This field will be required in a future release if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">EC</span></code> or <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>. The API will default to <code class="docutils literal notranslate"><span class="pre">P-256</span></code> if nothing is specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>key_opts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of JSON web key operations. Possible values include: <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>. Please note these values are case sensitive.</p></li>
<li><p><strong>key_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. <em>Note</em>: This field is required if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Key Type to use for this Key Vault Key. Possible values are <code class="docutils literal notranslate"><span class="pre">EC</span></code> (Elliptic Curve), <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>, <code class="docutils literal notranslate"><span class="pre">Oct</span></code> (Octet), <code class="docutils literal notranslate"><span class="pre">RSA</span></code> and <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_before_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.curve">
<code class="sig-name descname">curve</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.curve" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the curve to use when creating an <code class="docutils literal notranslate"><span class="pre">EC</span></code> key. Possible values are <code class="docutils literal notranslate"><span class="pre">P-256</span></code>, <code class="docutils literal notranslate"><span class="pre">P-384</span></code>, <code class="docutils literal notranslate"><span class="pre">P-521</span></code>, and <code class="docutils literal notranslate"><span class="pre">SECP256K1</span></code>. This field will be required in a future release if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">EC</span></code> or <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>. The API will default to <code class="docutils literal notranslate"><span class="pre">P-256</span></code> if nothing is specified. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.e">
<code class="sig-name descname">e</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.e" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA public exponent of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_opts">
<code class="sig-name descname">key_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of JSON web key operations. Possible values include: <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>. Please note these values are case sensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_size">
<code class="sig-name descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. <em>Note</em>: This field is required if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_type">
<code class="sig-name descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Key Type to use for this Key Vault Key. Possible values are <code class="docutils literal notranslate"><span class="pre">EC</span></code> (Elliptic Curve), <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>, <code class="docutils literal notranslate"><span class="pre">Oct</span></code> (Octet), <code class="docutils literal notranslate"><span class="pre">RSA</span></code> and <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.n">
<code class="sig-name descname">n</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.n" title="Permalink to this definition">¶</a></dt>
<dd><p>The RSA modulus of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.not_before_date">
<code class="sig-name descname">not_before_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.not_before_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.x">
<code class="sig-name descname">x</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.x" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC X component of this Key Vault Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Key.y">
<code class="sig-name descname">y</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Key.y" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC Y component of this Key Vault Key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Key.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">curve=None</em>, <em class="sig-param">e=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">key_opts=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">n=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_before_date=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">x=None</em>, <em class="sig-param">y=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Key resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the curve to use when creating an <code class="docutils literal notranslate"><span class="pre">EC</span></code> key. Possible values are <code class="docutils literal notranslate"><span class="pre">P-256</span></code>, <code class="docutils literal notranslate"><span class="pre">P-384</span></code>, <code class="docutils literal notranslate"><span class="pre">P-521</span></code>, and <code class="docutils literal notranslate"><span class="pre">SECP256K1</span></code>. This field will be required in a future release if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">EC</span></code> or <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>. The API will default to <code class="docutils literal notranslate"><span class="pre">P-256</span></code> if nothing is specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>e</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RSA public exponent of this Key Vault Key.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>key_opts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of JSON web key operations. Possible values include: <code class="docutils literal notranslate"><span class="pre">decrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">encrypt</span></code>, <code class="docutils literal notranslate"><span class="pre">sign</span></code>, <code class="docutils literal notranslate"><span class="pre">unwrapKey</span></code>, <code class="docutils literal notranslate"><span class="pre">verify</span></code> and <code class="docutils literal notranslate"><span class="pre">wrapKey</span></code>. Please note these values are case sensitive.</p></li>
<li><p><strong>key_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. <em>Note</em>: This field is required if <code class="docutils literal notranslate"><span class="pre">key_type</span></code> is <code class="docutils literal notranslate"><span class="pre">RSA</span></code> or <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Key Type to use for this Key Vault Key. Possible values are <code class="docutils literal notranslate"><span class="pre">EC</span></code> (Elliptic Curve), <code class="docutils literal notranslate"><span class="pre">EC-HSM</span></code>, <code class="docutils literal notranslate"><span class="pre">Oct</span></code> (Octet), <code class="docutils literal notranslate"><span class="pre">RSA</span></code> and <code class="docutils literal notranslate"><span class="pre">RSA-HSM</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>n</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RSA modulus of this Key Vault Key.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_before_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the Key Vault Key.</p></li>
<li><p><strong>x</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC X component of this Key Vault Key.</p></li>
<li><p><strong>y</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC Y component of this Key Vault Key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Key.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Key.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.KeyVault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">KeyVault</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">enabled_for_deployment=None</em>, <em class="sig-param">enabled_for_disk_encryption=None</em>, <em class="sig-param">enabled_for_template_deployment=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_acls=None</em>, <em class="sig-param">purge_protection_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">soft_delete_enabled=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KeyVault resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] access_policies: <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">A list</a> of up to 16 objects describing access policies, as described below.
:param pulumi.Input[bool] enabled_for_deployment: Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[bool] enabled_for_disk_encryption: Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[bool] enabled_for_template_deployment: Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Key Vault. Changing this forces a new resource to be created.
:param pulumi.Input[dict] network_acls: A <code class="docutils literal notranslate"><span class="pre">network_acls</span></code> block as defined below.
:param pulumi.Input[bool] purge_protection_enabled: Is Purge Protection enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.
:param pulumi.Input[str] sku_name: The Name of the SKU used for this Key Vault. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">premium</span></code>.
:param pulumi.Input[bool] soft_delete_enabled: Should Soft Delete be enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] tenant_id: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p>
<p>The <strong>access_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">application_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p></li>
</ul>
<p>The <strong>network_acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.access_policies">
<code class="sig-name descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">A list</a> of up to 16 objects describing access policies, as described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">application_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_deployment">
<code class="sig-name descname">enabled_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_disk_encryption">
<code class="sig-name descname">enabled_for_disk_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_disk_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.enabled_for_template_deployment">
<code class="sig-name descname">enabled_for_template_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.enabled_for_template_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.network_acls">
<code class="sig-name descname">network_acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.network_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_acls</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.purge_protection_enabled">
<code class="sig-name descname">purge_protection_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.purge_protection_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Purge Protection enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the SKU used for this Key Vault. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.soft_delete_enabled">
<code class="sig-name descname">soft_delete_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.soft_delete_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Soft Delete be enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.KeyVault.vault_uri">
<code class="sig-name descname">vault_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.vault_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Key Vault, used for performing operations on keys and secrets.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.KeyVault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">enabled_for_deployment=None</em>, <em class="sig-param">enabled_for_disk_encryption=None</em>, <em class="sig-param">enabled_for_template_deployment=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_acls=None</em>, <em class="sig-param">purge_protection_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">soft_delete_enabled=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">vault_uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyVault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p><a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">A list</a> of up to 16 objects describing access policies, as described below.</p>
</p></li>
<li><p><strong>enabled_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled_for_disk_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled_for_template_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_acls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_acls</span></code> block as defined below.</p></li>
<li><p><strong>purge_protection_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Purge Protection enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the SKU used for this Key Vault. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">premium</span></code>.</p></li>
<li><p><strong>soft_delete_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Soft Delete be enabled for this Key Vault? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p></li>
<li><p><strong>vault_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Key Vault, used for performing operations on keys and secrets.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">application_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.</p></li>
</ul>
<p>The <strong>network_acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.KeyVault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.KeyVault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.KeyVault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Secret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">Secret</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_before_date=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Key Vault Secret.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_secret.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/key_vault_secret.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the content type for the Key Vault Secret.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Secret should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_before_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the Key Vault Secret.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the content type for the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key Vault where the Secret should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.not_before_date">
<code class="sig-name descname">not_before_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.not_before_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the Key Vault Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.keyvault.Secret.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.keyvault.Secret.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the Key Vault Secret.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Secret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_before_date=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Secret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the content type for the Key Vault Secret.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault where the Secret should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_before_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key not usable before the provided UTC datetime (Y-m-d’T’H:M:S’Z’).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the Key Vault Secret.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the Key Vault Secret.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.keyvault.Secret.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.Secret.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.keyvault.get_access_policy">
<code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">get_access_policy</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the permissions from the Management Key Vault Templates.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Management Template. Possible values are: <code class="docutils literal notranslate"><span class="pre">Key</span> <span class="pre">Management</span></code>,
<code class="docutils literal notranslate"><span class="pre">Secret</span> <span class="pre">Management</span></code>, <code class="docutils literal notranslate"><span class="pre">Certificate</span> <span class="pre">Management</span></code>, <code class="docutils literal notranslate"><span class="pre">Key</span> <span class="pre">&amp;</span> <span class="pre">Secret</span> <span class="pre">Management</span></code>, <code class="docutils literal notranslate"><span class="pre">Key</span> <span class="pre">&amp;</span> <span class="pre">Certificate</span> <span class="pre">Management</span></code>,
<code class="docutils literal notranslate"><span class="pre">Secret</span> <span class="pre">&amp;</span> <span class="pre">Certificate</span> <span class="pre">Management</span></code>,  <code class="docutils literal notranslate"><span class="pre">Key,</span> <span class="pre">Secret,</span> <span class="pre">&amp;</span> <span class="pre">Certificate</span> <span class="pre">Management</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_key">
<code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">get_key</code><span class="sig-paren">(</span><em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault Key.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_key.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_vault_id</strong> (<em>str</em>) – Specifies the ID of the Key Vault instance where the Secret resides, available on the <code class="docutils literal notranslate"><span class="pre">keyvault.KeyVault</span></code> Data Source / Resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Key Vault Key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_key_vault">
<code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">get_key_vault</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_key_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Key Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Key Vault exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.keyvault.get_secret">
<code class="sig-prename descclassname">pulumi_azure.keyvault.</code><code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param">key_vault_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.keyvault.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Key Vault Secret.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the secret value will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_secret.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/key_vault_secret.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_vault_id</strong> (<em>str</em>) – Specifies the ID of the Key Vault instance where the Secret resides, available on the <code class="docutils literal notranslate"><span class="pre">keyvault.KeyVault</span></code> Data Source / Resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Key Vault Secret.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
