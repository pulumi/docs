---
---

<div class="section" id="module-pulumi_gcp.organizations">
<span id="organizations"></span><h1>organizations<a class="headerlink" href="#module-pulumi_gcp.organizations" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.organizations.Folder">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">Folder</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>display_name=None</em>, <em>parent=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Folder" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a Google Cloud Platform folder. For more information see 
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/creating-managing-folders">the official documentation</a>
and 
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v2/folders">API</a>.</p>
<p>A folder can contain projects, other folders, or a combination of both. You can use folders to group projects under an organization in a hierarchy. For example, your organization might contain multiple departments, each with its own set of Cloud Platform resources. Folders allows you to group these resources on a per-department basis. Folders are used to group resources that share common IAM policies.</p>
<p>Folders created live inside an Organization. See the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/quickstarts">Organization documentation</a> for more details.</p>
<p>The service account used to run Terraform when creating a <code class="docutils literal notranslate"><span class="pre">google_folder</span></code>
resource must have <code class="docutils literal notranslate"><span class="pre">roles/resourcemanager.folderCreator</span></code>. See the
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/access-control-folders">Access Control for Folders Using IAM</a>
doc for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.</li>
<li><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the parent Folder or Organization.
Must be of the form <code class="docutils literal notranslate"><span class="pre">folders/{folder_id}</span></code> or <code class="docutils literal notranslate"><span class="pre">organizations/{org_id}</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.Folder.create_time">
<code class="descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Folder.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp when the Folder was created. Assigned by the server.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Folder.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Folder.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Folder.lifecycle_state">
<code class="descname">lifecycle_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Folder.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The lifecycle state of the folder such as <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> or <code class="docutils literal notranslate"><span class="pre">DELETE_REQUESTED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Folder.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Folder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the Folder. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Folder.parent">
<code class="descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Folder.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the parent Folder or Organization.
Must be of the form <code class="docutils literal notranslate"><span class="pre">folders/{folder_id}</span></code> or <code class="docutils literal notranslate"><span class="pre">organizations/{org_id}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.Folder.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Folder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.Folder.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Folder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.GetActiveFolderResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetActiveFolderResult</code><span class="sig-paren">(</span><em>display_name=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetActiveFolderResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActiveFolder.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetActiveFolderResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetActiveFolderResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the Folder. This uniquely identifies the folder.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetActiveFolderResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetActiveFolderResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetBillingAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetBillingAccountResult</code><span class="sig-paren">(</span><em>billing_account=None</em>, <em>display_name=None</em>, <em>name=None</em>, <em>open=None</em>, <em>project_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetBillingAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBillingAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetBillingAccountResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetBillingAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the billing account in the form <code class="docutils literal notranslate"><span class="pre">billingAccounts/{billing_account_id}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetBillingAccountResult.project_ids">
<code class="descname">project_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetBillingAccountResult.project_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of any projects associated with the billing account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetBillingAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetBillingAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetClientConfigResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetClientConfigResult</code><span class="sig-paren">(</span><em>access_token=None</em>, <em>project=None</em>, <em>region=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientConfigResult.access_token">
<code class="descname">access_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientConfigResult.access_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAuth2 access token used by the client to authenticate against the Google Cloud API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientConfigResult.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientConfigResult.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to apply any resources to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientConfigResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientConfigResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region to operate under.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientConfigResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetClientOpenIdUserInfoResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetClientOpenIdUserInfoResult</code><span class="sig-paren">(</span><em>email=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetClientOpenIdUserInfoResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientOpenIdUserInfo.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientOpenIdUserInfoResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientOpenIdUserInfoResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of the account used by the provider to authenticate with GCP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetClientOpenIdUserInfoResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetClientOpenIdUserInfoResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetFolderResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetFolderResult</code><span class="sig-paren">(</span><em>create_time=None</em>, <em>display_name=None</em>, <em>folder=None</em>, <em>lifecycle_state=None</em>, <em>lookup_organization=None</em>, <em>name=None</em>, <em>organization=None</em>, <em>parent=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFolder.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.create_time">
<code class="descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp when the Organization was created. A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.lifecycle_state">
<code class="descname">lifecycle_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The Folder’s current lifecycle state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the Folder in the form <code class="docutils literal notranslate"><span class="pre">folders/{folder_id}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.organization">
<code class="descname">organization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">lookup_organization</span></code> is enable, the resource name of the Organization that the folder belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.parent">
<code class="descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the parent Folder or Organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetFolderResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetFolderResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetIAMPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetIAMPolicyResult</code><span class="sig-paren">(</span><em>audit_configs=None</em>, <em>bindings=None</em>, <em>policy_data=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetIAMPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIAMPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetIAMPolicyResult.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetIAMPolicyResult.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetIAMPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetIAMPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetOrganizationResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetOrganizationResult</code><span class="sig-paren">(</span><em>create_time=None</em>, <em>directory_customer_id=None</em>, <em>domain=None</em>, <em>lifecycle_state=None</em>, <em>name=None</em>, <em>organization=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganization.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetOrganizationResult.create_time">
<code class="descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp when the Organization was created. A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetOrganizationResult.directory_customer_id">
<code class="descname">directory_customer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult.directory_customer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google for Work customer ID of the Organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetOrganizationResult.lifecycle_state">
<code class="descname">lifecycle_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The Organization’s current lifecycle state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetOrganizationResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the Organization in the form <code class="docutils literal notranslate"><span class="pre">organizations/{organization_id}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetOrganizationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetOrganizationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetProjectResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetProjectResult</code><span class="sig-paren">(</span><em>app_engines=None</em>, <em>auto_create_network=None</em>, <em>billing_account=None</em>, <em>folder_id=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>number=None</em>, <em>org_id=None</em>, <em>policy_data=None</em>, <em>policy_etag=None</em>, <em>project_id=None</em>, <em>skip_delete=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetProjectResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.GetProjectServicesResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">GetProjectServicesResult</code><span class="sig-paren">(</span><em>disable_on_destroy=None</em>, <em>project=None</em>, <em>services=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.GetProjectServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectServices.</p>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.GetProjectServicesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.GetProjectServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.organizations.IAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">IAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>org_id=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Organization.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_organization_iam_member</span></code> for the <strong>same role</strong> or they will fight over
what your policy should be.</dd>
<dt><strong>Note:</strong> On create, this resource will overwrite members of any existing roles.</dt>
<dd>Use <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">import</span></code> and inspect the <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">plan</span></code> output to ensure
your existing members are preserved.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization in which you want to create a custom role.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_organization_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMBinding.members">
<code class="descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMBinding.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization in which you want to create a custom role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_organization_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.IAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMCustomRole">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">IAMCustomRole</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>org_id=None</em>, <em>permissions=None</em>, <em>role_id=None</em>, <em>stage=None</em>, <em>title=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a customized Cloud IAM organization role. For more information see
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-custom-roles">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles">API</a>.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Warning:</strong> Note that custom roles in GCP have the concept of a soft-delete. There are two issues that may arise</dt>
<dd>from this and how roles are propagated. 1) creating a role may involve undeleting and then updating a role with the
same name, possibly causing confusing behavior between undelete and update. 2) A deleted role is permanently deleted
after 7 days, but it can take up to 30 more days (i.e. between 7 and 37 days after deletion) before the role name is
made available again. This means a deleted role that has been deleted for more than 7 days cannot be changed at all
by Terraform, and new roles cannot share that name.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the role.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization in which you want to create a custom role.</li>
<li><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</li>
<li><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role id to use for this role.</li>
<li><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</li>
<li><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable title for the role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.deleted">
<code class="descname">deleted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.deleted" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The current deleted state of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization in which you want to create a custom role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.role_id">
<code class="descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role id to use for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.stage">
<code class="descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMCustomRole.title">
<code class="descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable title for the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.IAMCustomRole.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMCustomRole.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMCustomRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">IAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>org_id=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Organization.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_organization_iam_binding</span></code> for the <strong>same role</strong> or they will fight over
what your policy should be.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization in which you want to create a custom role.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMMember.member">
<code class="descname">member</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.member" title="Permalink to this definition">¶</a></dt>
<dd><p>The user that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMMember.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization in which you want to create a custom role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.IAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">IAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>org_id=None</em>, <em>policy_data=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of the entire IAM policy for an existing Google Cloud Platform Organization.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Warning:</strong> New organizations have several default policies which will,</dt>
<dd>without extreme caution, be <strong>overwritten</strong> by use of this resource.
The safest alternative is to use multiple <code class="docutils literal notranslate"><span class="pre">google_organization_iam_binding</span></code>
resources.  It is easy to use this resource to remove your own access to
an organization, which will require a call to Google Support to have
fixed, and can take multiple days to resolve.  If you do use this resource,
the best way to be sure that you are not making dangerous changes is to start
by importing your existing policy, and examining the diff very closely.</dd>
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_organization_iam_member</span></code> or <code class="docutils literal notranslate"><span class="pre">google_organization_iam_binding</span></code>
or they will fight over what your policy should be.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization in which you want to create a custom role.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMPolicy.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMPolicy.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization in which you want to create a custom role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.IAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.IAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.IAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.Policy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>boolean_policy=None</em>, <em>constraint=None</em>, <em>list_policy=None</em>, <em>org_id=None</em>, <em>restore_policy=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Organization. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</li>
<li><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</li>
<li><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization to set the policy for.</li>
<li><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.boolean_policy">
<code class="descname">boolean_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.boolean_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.constraint">
<code class="descname">constraint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.constraint" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.list_policy">
<code class="descname">list_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.list_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization to set the policy for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.restore_policy">
<code class="descname">restore_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.restore_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A restore policy is a constraint to restore the default policy. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.update_time">
<code class="descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Policy.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Policy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the Policy. Default version is 0.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.Project">
<em class="property">class </em><code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_create_network=None</em>, <em>billing_account=None</em>, <em>folder_id=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>org_id=None</em>, <em>project_id=None</em>, <em>skip_delete=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a Google Cloud Platform project.</p>
<p>Projects created with this resource must be associated with an Organization.
See the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/quickstarts">Organization documentation</a> for more details.</p>
<p>The service account used to run Terraform when creating a <code class="docutils literal notranslate"><span class="pre">google_project</span></code>
resource must have <code class="docutils literal notranslate"><span class="pre">roles/resourcemanager.projectCreator</span></code>. See the
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/access-control-org">Access Control for Organizations Using IAM</a>
doc for more information.</p>
<p>Note that prior to 0.8.5, <code class="docutils literal notranslate"><span class="pre">google_project</span></code> functioned like a data source,
meaning any project referenced by it had to be created and managed outside
Terraform. As of 0.8.5, <code class="docutils literal notranslate"><span class="pre">google_project</span></code> functions like any other Terraform
resource, with Terraform creating and managing the project. To replicate the old
behavior, either:</p>
<ul class="simple">
<li>Use the project ID directly in whatever is referencing the project, using the
<a class="reference external" href="https://www.terraform.io/docs/providers/google/r/google_project_iam.html">google_project_iam_policy</a>
to replace the old <code class="docutils literal notranslate"><span class="pre">policy_data</span></code> property.</li>
<li>Use the <a class="reference external" href="https://www.terraform.io/docs/import/usage.html">import</a> functionality
to import your pre-existing project into Terraform, where it can be referenced and
used just like always, keeping in mind that Terraform will attempt to undo any changes
made outside Terraform.</li>
</ul>
<blockquote>
<div>It’s important to note that any project resources that were added to your Terraform config
prior to 0.8.5 will continue to function as they always have, and will not be managed by
Terraform. Only newly added projects are affected.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_create_network</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create the ‘default’ network automatically.  Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.
If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the default network will be deleted.  Note that, for quota purposes, you
will still need to have 1 network slot available to create the project succesfully, even if
you set <code class="docutils literal notranslate"><span class="pre">auto_create_network</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code>, since the network will exist momentarily.</li>
<li><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (<code class="docutils literal notranslate"><span class="pre">roles/billing.admin</span></code>) in
the organization. See <a class="reference external" href="https://cloud.google.com/billing/v1/how-tos/access-control">Google Cloud Billing API Access Control</a>
for more details.</li>
<li><strong>folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the folder this project should be
created under. Only one of <code class="docutils literal notranslate"><span class="pre">org_id</span></code> or <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> may be
specified. If the <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the project.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the project.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
<code class="docutils literal notranslate"><span class="pre">org_id</span></code> or <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> may be specified. If the <code class="docutils literal notranslate"><span class="pre">org_id</span></code> is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. Changing this forces a new project to be created.</li>
<li><strong>skip_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the Terraform resource can be deleted
without deleting the Project via the Google API.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.auto_create_network">
<code class="descname">auto_create_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.auto_create_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Create the ‘default’ network automatically.  Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.
If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the default network will be deleted.  Note that, for quota purposes, you
will still need to have 1 network slot available to create the project succesfully, even if
you set <code class="docutils literal notranslate"><span class="pre">auto_create_network</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code>, since the network will exist momentarily.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.billing_account">
<code class="descname">billing_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (<code class="docutils literal notranslate"><span class="pre">roles/billing.admin</span></code>) in
the organization. See <a class="reference external" href="https://cloud.google.com/billing/v1/how-tos/access-control">Google Cloud Billing API Access Control</a>
for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.folder_id">
<code class="descname">folder_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.folder_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the folder this project should be
created under. Only one of <code class="docutils literal notranslate"><span class="pre">org_id</span></code> or <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> may be
specified. If the <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.number">
<code class="descname">number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.number" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric identifier of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
<code class="docutils literal notranslate"><span class="pre">org_id</span></code> or <code class="docutils literal notranslate"><span class="pre">folder_id</span></code> may be specified. If the <code class="docutils literal notranslate"><span class="pre">org_id</span></code> is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. Changing this forces a new project to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.organizations.Project.skip_delete">
<code class="descname">skip_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.organizations.Project.skip_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the Terraform resource can be deleted
without deleting the Project via the Google API.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.organizations.Project.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.Project.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.organizations.get_active_folder">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_active_folder</code><span class="sig-paren">(</span><em>display_name=None</em>, <em>parent=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_active_folder" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an active folder within GCP by <code class="docutils literal notranslate"><span class="pre">display_name</span></code> and <code class="docutils literal notranslate"><span class="pre">parent</span></code>.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_billing_account">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_billing_account</code><span class="sig-paren">(</span><em>billing_account=None</em>, <em>display_name=None</em>, <em>open=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google Billing Account.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_client_config">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_client_config</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the configuration of the Google Cloud provider.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_client_open_id_user_info">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_client_open_id_user_info</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_client_open_id_user_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get OpenID userinfo about the credentials used with the Google provider,
specifically the email.</p>
<p>When the <code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/auth/userinfo.email</span></code> scope is enabled in
your provider block, this datasource enables you to export the email of the
account you’ve authenticated the provider with; this can be used alongside
<code class="docutils literal notranslate"><span class="pre">data.google_client_config</span></code>’s <code class="docutils literal notranslate"><span class="pre">access_token</span></code> to perform OpenID Connect
authentication with GKE and configure an RBAC role for the email used.</p>
<blockquote>
<div>This resource will only work as expected if the provider is configured to
use the <code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/auth/userinfo.email</span></code> scope! You will
receive an error otherwise.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_folder">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_folder</code><span class="sig-paren">(</span><em>folder=None</em>, <em>lookup_organization=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_folder" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google Cloud Folder.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_iam_policy">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_iam_policy</code><span class="sig-paren">(</span><em>audit_configs=None</em>, <em>bindings=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_iam_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Generates an IAM policy document that may be referenced by and applied to
other Google Cloud Platform resources, such as the <code class="docutils literal notranslate"><span class="pre">google_project</span></code> resource.</p>
<p>This data source is used to define IAM policies to apply to other resources.
Currently, defining a policy through a datasource and referencing that policy
from another resource is the only way to apply an IAM policy to a resource.</p>
<p><strong>Note:</strong> Several restrictions apply when setting IAM policies through this API.
See the <a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy">setIamPolicy docs</a>
for a list of these restrictions.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_organization">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_organization</code><span class="sig-paren">(</span><em>domain=None</em>, <em>organization=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google Cloud Organization.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_project">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_project</code><span class="sig-paren">(</span><em>project_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get project details.
For more information see 
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project">API</a></p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.organizations.get_project_services">
<code class="descclassname">pulumi_gcp.organizations.</code><code class="descname">get_project_services</code><span class="sig-paren">(</span><em>project=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.organizations.get_project_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get details on the enabled project services.</p>
<p>For a list of services available, visit the
<a class="reference external" href="https://console.cloud.google.com/apis/library">API library page</a> or run <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">services</span> <span class="pre">list</span></code>.</p>
</dd></dl>

</div>
