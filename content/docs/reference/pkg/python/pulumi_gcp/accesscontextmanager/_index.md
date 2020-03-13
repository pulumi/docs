---
title: Module accesscontextmanager
title_tag: Module accesscontextmanager | Package pulumi_gcp | Python SDK
linktitle: accesscontextmanager
notitle: true
---

<div class="section" id="accesscontextmanager">
<h1>accesscontextmanager<a class="headerlink" href="#accesscontextmanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.accesscontextmanager"></span><dl class="class">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.accesscontextmanager.</code><code class="sig-name descname">AccessLevel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel" title="Permalink to this definition">¶</a></dt>
<dd><p>An AccessLevel is a label that can be applied to requests to GCP services,
along with a list of requirements necessary for the label to be applied.</p>
<p>To get more information about AccessLevel, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/quickstart">Access Policy Quickstart</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>basic</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of predefined conditions for the access level and a combining function.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the AccessLevel and its use. Does not affect behavior.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name for the Access Level. The short<em>name component must begin with a letter and only include alphanumeric and
‘</em>’. Format: accessPolicies/{policy_id}/accessLevels/{short_name}</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Must be unique within the Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">combiningFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devicePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDeviceManagementLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedEncryptionStatuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAdminApproval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCorpOwned</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireScreenLock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipSubnetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAccessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.basic">
<code class="sig-name descname">basic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.basic" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of predefined conditions for the access level and a combining function.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">combiningFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devicePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDeviceManagementLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedEncryptionStatuses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAdminApproval</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCorpOwned</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireScreenLock</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipSubnetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAccessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the AccessLevel and its use. Does not affect behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name for the Access Level. The short<em>name component must begin with a letter and only include alphanumeric and
‘</em>’. Format: accessPolicies/{policy_id}/accessLevels/{short_name}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable title. Must be unique within the Policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">title=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessLevel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>basic</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of predefined conditions for the access level and a combining function.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the AccessLevel and its use. Does not affect behavior.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name for the Access Level. The short<em>name component must begin with a letter and only include alphanumeric and
‘</em>’. Format: accessPolicies/{policy_id}/accessLevels/{short_name}</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Must be unique within the Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">combiningFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devicePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDeviceManagementLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedEncryptionStatuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAdminApproval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCorpOwned</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireScreenLock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipSubnetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">members</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAccessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.accesscontextmanager.</code><code class="sig-name descname">AccessPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>AccessPolicy is a container for AccessLevels (which define the necessary
attributes to use GCP services) and ServicePerimeters (which define
regions of services able to freely pass data within a perimeter). An
access policy is globally visible within an organization, and the
restrictions it specifies apply to all projects within an organization.</p>
<p>To get more information about AccessPolicy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/quickstart">Access Policy Quickstart</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent of this AccessPolicy in the Cloud Resource Hierarchy. Format: organizations/{organization_id}</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Does not affect behavior.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time the AccessPolicy was created in UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name of the AccessPolicy. Format: {policy_id}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent of this AccessPolicy in the Cloud Resource Hierarchy. Format: organizations/{organization_id}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable title. Does not affect behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time the AccessPolicy was updated in UTC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time the AccessPolicy was created in UTC.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name of the AccessPolicy. Format: {policy_id}</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent of this AccessPolicy in the Cloud Resource Hierarchy. Format: organizations/{organization_id}</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Does not affect behavior.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time the AccessPolicy was updated in UTC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.accesscontextmanager.</code><code class="sig-name descname">ServicePerimeter</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">perimeter_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter" title="Permalink to this definition">¶</a></dt>
<dd><p>ServicePerimeter describes a set of GCP resources which can freely import
and export data amongst themselves, but not export outside of the
ServicePerimeter. If a request with a source within this ServicePerimeter
has a target outside of the ServicePerimeter, the request will be blocked.
Otherwise the request is allowed. There are two types of Service Perimeter</p>
<ul class="simple">
<li><p>Regular and Bridge. Regular Service Perimeters cannot overlap, a single
GCP project can only belong to a single regular Service Perimeter. Service
Perimeter Bridges can contain only GCP projects as members, a single GCP
project may belong to multiple Service Perimeter Bridges.</p></li>
</ul>
<p>To get more information about ServicePerimeter, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc-service-controls/docs/quickstart">Service Perimeter Quickstart</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the ServicePerimeter and its use. Does not affect behavior.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name for the ServicePerimeter. The short<em>name component must begin with a letter and only include alphanumeric
and ‘</em>’. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}</p></li>
<li><p><strong>perimeter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
(whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
data among themselves.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
perimeter content and boundaries.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Must be unique within the Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictedServices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time the AccessPolicy was created in UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the ServicePerimeter and its use. Does not affect behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name for the ServicePerimeter. The short<em>name component must begin with a letter and only include alphanumeric
and ‘</em>’. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.perimeter_type">
<code class="sig-name descname">perimeter_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.perimeter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
(whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
data among themselves.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.status" title="Permalink to this definition">¶</a></dt>
<dd><p>ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
perimeter content and boundaries.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictedServices</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable title. Must be unique within the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time the AccessPolicy was updated in UTC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">perimeter_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePerimeter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time the AccessPolicy was created in UTC.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the ServicePerimeter and its use. Does not affect behavior.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name for the ServicePerimeter. The short<em>name component must begin with a letter and only include alphanumeric
and ‘</em>’. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}</p></li>
<li><p><strong>perimeter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
(whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
data among themselves.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
perimeter content and boundaries.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable title. Must be unique within the Policy.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time the AccessPolicy was updated in UTC.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restrictedServices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.accesscontextmanager.</code><code class="sig-name descname">ServicePerimeterResource</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">perimeter_name=None</em>, <em class="sig-param">resource=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows configuring a single GCP resource that should be inside of a service perimeter.
This resource is intended to be used in cases where it is not possible to compile a full list
of projects to include in a <code class="docutils literal notranslate"><span class="pre">accesscontextmanager.ServicePerimeter</span></code> resource,
to enable them to be added separately.</p>
<blockquote>
<div><p><strong>Note:</strong> If this resource is used alongside a <code class="docutils literal notranslate"><span class="pre">accesscontextmanager.ServicePerimeter</span></code> resource,
the service perimeter resource must have a <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> block with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span> <span class="pre">=</span> <span class="pre">[status[0].resources]</span></code> so
they don’t fight over which resources should be in the policy.</p>
</div></blockquote>
<p>To get more information about ServicePerimeterResource, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc-service-controls/docs/quickstart">Service Perimeter Quickstart</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter_resource.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter_resource.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>perimeter_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Perimeter to add this resource to.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GCP resource that is inside of the service perimeter. Currently only projects are allowed. Format:
projects/{project_number}</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource.perimeter_name">
<code class="sig-name descname">perimeter_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource.perimeter_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Perimeter to add this resource to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource.resource">
<code class="sig-name descname">resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource.resource" title="Permalink to this definition">¶</a></dt>
<dd><p>A GCP resource that is inside of the service perimeter. Currently only projects are allowed. Format:
projects/{project_number}</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">perimeter_name=None</em>, <em class="sig-param">resource=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePerimeterResource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>perimeter_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Perimeter to add this resource to.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GCP resource that is inside of the service perimeter. Currently only projects are allowed. Format:
projects/{project_number}</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeterResource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeterResource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
