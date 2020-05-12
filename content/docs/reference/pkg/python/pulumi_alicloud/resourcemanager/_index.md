---
title: Module resourcemanager
title_tag: Module resourcemanager | Package pulumi_alicloud | Python SDK
linktitle: resourcemanager
notitle: true
---

<div class="section" id="resourcemanager">
<h1>resourcemanager<a class="headerlink" href="#resourcemanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.resourcemanager"></span><dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.Folder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">Folder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_folder_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Folder resource. A folder is an organizational unit in a resource directory. You can use folders to build an organizational structure for resources.
For information about Resource Manager Foler and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/111221.htm">What is Resource Manager Folder</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.82.0+.</p>
<p><strong>NOTE:</strong> A maximum of five levels of folders can be created under the root folder.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Folder</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">folder_name</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>folder*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (<a href="#id3"><span class="problematic" id="id4">*</span></a>), periods (.), and hyphens (-).</p>
</p></li>
<li><p><strong>parent_folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent folder. If not set, the system default value will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Folder.folder_name">
<code class="sig-name descname">folder_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder.folder_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Folder.parent_folder_id">
<code class="sig-name descname">parent_folder_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder.parent_folder_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the parent folder. If not set, the system default value will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Folder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_folder_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Folder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>folder*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>), periods (.), and hyphens (-).</p>
</p></li>
<li><p><strong>parent_folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent folder. If not set, the system default value will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Folder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Folder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Folder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Handshake">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">Handshake</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_entity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager handshake resource. You can invite accounts to join a resource directory for unified management.
For information about Resource Manager handshake and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/135287.htm">What is Resource Manager handshake</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.82.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Add a Resource Manager handshake.</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Handshake</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">note</span><span class="o">=</span><span class="s2">&quot;test resource manager handshake&quot;</span><span class="p">,</span>
    <span class="n">target_entity</span><span class="o">=</span><span class="s2">&quot;1182775234******&quot;</span><span class="p">,</span>
    <span class="n">target_type</span><span class="o">=</span><span class="s2">&quot;Account&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Remarks. The maximum length is 1024 characters.</p></li>
<li><p><strong>target_entity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Invited account ID or login email.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of account being invited. Valid values: <code class="docutils literal notranslate"><span class="pre">Account</span></code>, <code class="docutils literal notranslate"><span class="pre">Email</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.expire_time">
<code class="sig-name descname">expire_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.expire_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration time of the invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.master_account_id">
<code class="sig-name descname">master_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource account master account ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.master_account_name">
<code class="sig-name descname">master_account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.master_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the main account of the resource directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.modify_time">
<code class="sig-name descname">modify_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.modify_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The modification time of the invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.note">
<code class="sig-name descname">note</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.note" title="Permalink to this definition">¶</a></dt>
<dd><p>Remarks. The maximum length is 1024 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.resource_directory_id">
<code class="sig-name descname">resource_directory_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.resource_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource directory ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Invitation status. Valid values: <code class="docutils literal notranslate"><span class="pre">Pending</span></code> waiting for confirmation, <code class="docutils literal notranslate"><span class="pre">Accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">Declined</span></code>, <code class="docutils literal notranslate"><span class="pre">Expired</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.target_entity">
<code class="sig-name descname">target_entity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.target_entity" title="Permalink to this definition">¶</a></dt>
<dd><p>Invited account ID or login email.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Handshake.target_type">
<code class="sig-name descname">target_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.target_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of account being invited. Valid values: <code class="docutils literal notranslate"><span class="pre">Account</span></code>, <code class="docutils literal notranslate"><span class="pre">Email</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Handshake.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modify_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_entity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Handshake resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expire_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the invitation.</p></li>
<li><p><strong>master_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource account master account ID.</p></li>
<li><p><strong>master_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the main account of the resource directory.</p></li>
<li><p><strong>modify_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The modification time of the invitation.</p></li>
<li><p><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Remarks. The maximum length is 1024 characters.</p></li>
<li><p><strong>resource_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource directory ID.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Invitation status. Valid values: <code class="docutils literal notranslate"><span class="pre">Pending</span></code> waiting for confirmation, <code class="docutils literal notranslate"><span class="pre">Accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">Declined</span></code>, <code class="docutils literal notranslate"><span class="pre">Expired</span></code>.</p></li>
<li><p><strong>target_entity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Invited account ID or login email.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of account being invited. Valid values: <code class="docutils literal notranslate"><span class="pre">Account</span></code>, <code class="docutils literal notranslate"><span class="pre">Email</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Handshake.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Handshake.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Handshake.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">ResourceGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Resource Group resource. If you need to group cloud resources according to business departments, projects, and other dimensions, you can create resource groups.
For information about Resource Manager Resoource Group and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/94485.htm">What is Resource Manager Resource Group</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.82.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;testrd&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The display name of the resource group. The name must be 1 to 30 characters in length and can contain letters, digits, periods (.), at signs (&#64;), and hyphens (-).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the resource group.The identifier must be 3 to 12 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (<a href="#id11"><span class="problematic" id="id12">*</span></a>). The identifier must start with a letter.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Alibaba Cloud account to which the resource group belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.create_date">
<code class="sig-name descname">create_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the resource group was created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region_statuses</span></code> -The status of the resource group in all regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region_id</span></code> - The region ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The status of the regional resource group.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the resource group. The name must be 1 to 30 characters in length and can contain letters, digits, periods (.), at signs (&#64;), and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the resource group.The identifier must be 3 to 12 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The identifier must start with a letter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the resource group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_statuses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Alibaba Cloud account to which the resource group belongs.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the resource group was created.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `region_statuses` -The status of the resource group in all regions.
- `region_id` - The region ID.
- `status` - The status of the regional resource group.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The display name of the resource group. The name must be 1 to 30 characters in length and can contain letters, digits, periods (.), at signs (&#64;), and hyphens (-).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the resource group.The identifier must be 3 to 12 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (<a href="#id15"><span class="problematic" id="id16">*</span></a>). The identifier must start with a letter.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the resource group.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>region_statuses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the resource group.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.ResourceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assume_role_policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_session_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager role resource. Members are resource containers in the resource directory, which can physically isolate resources to form an independent resource grouping unit. You can create members in the resource folder to manage them in a unified manner.
For information about Resource Manager role and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/111231.htm">What is Resource Manager role</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.82.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Add a Resource Manager role.</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">assume_role_policy_document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;     {</span>
<span class="s2">          &quot;Statement&quot;: [</span>
<span class="s2">               {</span>
<span class="s2">                    &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">                    &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                    &quot;Principal&quot;: {</span>
<span class="s2">                        &quot;RAM&quot;:&quot;acs:ram::103755469187****:root&quot;</span>
<span class="s2">                    }</span>
<span class="s2">                }</span>
<span class="s2">          ],</span>
<span class="s2">          &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">     }</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;testrd&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assume_role_policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the permissions strategy that plays a role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Resource Manager role.</p></li>
<li><p><strong>max_session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Role maximum session time. Valid values: [3600-43200]. Default to <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role Name. The length is 1 ~ 64 characters, which can include English letters, numbers, dots “.” and dashes “-“.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource descriptor of the role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.assume_role_policy_document">
<code class="sig-name descname">assume_role_policy_document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.assume_role_policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>The content of the permissions strategy that plays a role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.create_date">
<code class="sig-name descname">create_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Role creation time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Resource Manager role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.max_session_duration">
<code class="sig-name descname">max_session_duration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.max_session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>Role maximum session time. Valid values: [3600-43200]. Default to <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Role Name. The length is 1 ~ 64 characters, which can include English letters, numbers, dots “.” and dashes “-“.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Role.update_date">
<code class="sig-name descname">update_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.update_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Role update time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assume_role_policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_session_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_date</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource descriptor of the role.</p></li>
<li><p><strong>assume_role_policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the permissions strategy that plays a role.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role creation time.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Resource Manager role.</p></li>
<li><p><strong>max_session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Role maximum session time. Valid values: [3600-43200]. Default to <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role Name. The length is 1 ~ 64 characters, which can include English letters, numbers, dots “.” and dashes “-“.</p></li>
<li><p><strong>update_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role update time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
