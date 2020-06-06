---
title: Module resourcemanager
title_tag: Module resourcemanager | Package pulumi_alicloud | Python SDK
linktitle: resourcemanager
notitle: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="resourcemanager">
<h1>resourcemanager<a class="headerlink" href="#resourcemanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.resourcemanager"></span><dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Account resource. Member accounts are containers for resources in a resource directory. These accounts isolate resources and serve as organizational units in the resource directory. You can create member accounts in a folder and then manage them in a unified manner.
For information about Resource Manager Account and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/111231.htm">What is Resource Manager Account</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.83.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Add a Resource Manager Account.</span>
<span class="n">f1</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Folder</span><span class="p">(</span><span class="s2">&quot;f1&quot;</span><span class="p">,</span> <span class="n">folder_name</span><span class="o">=</span><span class="s2">&quot;test1&quot;</span><span class="p">)</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;RDAccount&quot;</span><span class="p">,</span>
    <span class="n">folder_id</span><span class="o">=</span><span class="n">f1</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (<a href="#id3"><span class="problematic" id="id4">*</span></a>), dots (.) And dashes (-).</p>
</p></li>
<li><p><strong>folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent folder.</p></li>
<li><p><strong>payer_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Settlement account ID. If the value is empty, the current account will be used for settlement.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.folder_id">
<code class="sig-name descname">folder_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.folder_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the parent folder.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.join_method">
<code class="sig-name descname">join_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.join_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Ways for members to join the resource directory. Valid values: <code class="docutils literal notranslate"><span class="pre">invited</span></code>, <code class="docutils literal notranslate"><span class="pre">created</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.join_time">
<code class="sig-name descname">join_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.join_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the member joined the resource directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.modify_time">
<code class="sig-name descname">modify_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.modify_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The modification time of the invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.payer_account_id">
<code class="sig-name descname">payer_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.payer_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Settlement account ID. If the value is empty, the current account will be used for settlement.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.resource_directory_id">
<code class="sig-name descname">resource_directory_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.resource_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource directory ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Member joining status. Valid values: <code class="docutils literal notranslate"><span class="pre">CreateSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateVerifying</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateFailed</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateExpired</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateCancelled</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteVerifying</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteFailed</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteExpired</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteCancelled</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">InviteSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">Removed</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Account.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Member type. The value of <code class="docutils literal notranslate"><span class="pre">ResourceAccount</span></code> indicates the resource account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">join_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">join_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modify_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>), dots (.) And dashes (-).</p>
</p></li>
<li><p><strong>folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent folder.</p></li>
<li><p><strong>join_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ways for members to join the resource directory. Valid values: <code class="docutils literal notranslate"><span class="pre">invited</span></code>, <code class="docutils literal notranslate"><span class="pre">created</span></code>.</p></li>
<li><p><strong>join_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the member joined the resource directory.</p></li>
<li><p><strong>modify_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The modification time of the invitation.</p></li>
<li><p><strong>payer_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Settlement account ID. If the value is empty, the current account will be used for settlement.</p></li>
<li><p><strong>resource_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource directory ID.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Member joining status. Valid values: <code class="docutils literal notranslate"><span class="pre">CreateSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateVerifying</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateFailed</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateExpired</span></code>,<code class="docutils literal notranslate"><span class="pre">CreateCancelled</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteVerifying</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteFailed</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteExpired</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteCancelled</span></code>,<code class="docutils literal notranslate"><span class="pre">PromoteSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">InviteSuccess</span></code>,<code class="docutils literal notranslate"><span class="pre">Removed</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Member type. The value of <code class="docutils literal notranslate"><span class="pre">ResourceAccount</span></code> indicates the resource account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetAccountsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetAccountsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetAccountsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetFoldersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetFoldersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">folders</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_folder_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetFoldersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetHandshakesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetHandshakesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">handshakes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetHandshakesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetPolicyVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetPolicyVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetPolicyVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetResourceDirectoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetResourceDirectoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">directories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetResourceDirectoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetResourceGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetResourceGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetResourceGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.AwaitableGetRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">AwaitableGetRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.AwaitableGetRolesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
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
<li><p><strong>folder*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (<a href="#id11"><span class="problematic" id="id12">*</span></a>), periods (.), and hyphens (-).</p>
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
<li><p><strong>folder*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (<a href="#id15"><span class="problematic" id="id16">*</span></a>), periods (.), and hyphens (-).</p>
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
<dt id="pulumi_alicloud.resourcemanager.GetAccountsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetAccountsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetAccountsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccounts.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetAccountsResult.accounts">
<code class="sig-name descname">accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetAccountsResult.accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of accounts. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetAccountsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetAccountsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetAccountsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetAccountsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of account IDs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetFoldersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetFoldersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">folders</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_folder_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetFoldersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFolders.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetFoldersResult.folders">
<code class="sig-name descname">folders</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetFoldersResult.folders" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of folders. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetFoldersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetFoldersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetFoldersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetFoldersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of folder IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetFoldersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetFoldersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of folder names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetHandshakesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetHandshakesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">handshakes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetHandshakesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getHandshakes.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetHandshakesResult.handshakes">
<code class="sig-name descname">handshakes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetHandshakesResult.handshakes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Resource Manager Handshakes. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetHandshakesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetHandshakesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetHandshakesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetHandshakesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Resource Manager Handshake IDs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicies.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPoliciesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPoliciesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPoliciesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPoliciesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPoliciesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPoliciesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPoliciesResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPoliciesResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetPolicyVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetPolicyVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPolicyVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyVersions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy version IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetPolicyVersionsResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy versions. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetResourceDirectoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">directories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceDirectories.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult.directories">
<code class="sig-name descname">directories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult.directories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of resource directories. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceDirectoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetResourceGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of resource groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of resource group IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of resource group names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetResourceGroupsResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetResourceGroupsResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the resource group. Possible values:<code class="docutils literal notranslate"><span class="pre">Creating</span></code>,<code class="docutils literal notranslate"><span class="pre">Deleted</span></code>,<code class="docutils literal notranslate"><span class="pre">OK</span></code> and <code class="docutils literal notranslate"><span class="pre">PendingDelete</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.resourcemanager.GetRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">GetRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetRolesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRoles.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetRolesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetRolesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetRolesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetRolesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of role IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetRolesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetRolesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of role names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.GetRolesResult.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.GetRolesResult.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of roles. Each element contains the following attributes:</p>
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
<dt id="pulumi_alicloud.resourcemanager.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Policy resource.<span class="raw-html-m2r"><br></span>
For information about Resource Manager Policy and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/93732.htm">What is Resource Manager Policy</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.83.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">policy_document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;         {</span>
<span class="s2">                        &quot;Statement&quot;: [{</span>
<span class="s2">                                &quot;Action&quot;: [&quot;oss:*&quot;],</span>
<span class="s2">                                &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                                &quot;Resource&quot;: [&quot;acs:oss:*:*:*&quot;]</span>
<span class="s2">                        }],</span>
<span class="s2">                        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">                }</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">policy_name</span><span class="o">=</span><span class="s2">&quot;abc12345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the policy. Default to v1.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy. The description must be 1 to 1,024 characters in length.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the policy. The content must be 1 to 2,048 characters in length.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.create_date">
<code class="sig-name descname">create_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the policy was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.default_version">
<code class="sig-name descname">default_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the policy. Default to v1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy. The description must be 1 to 1,024 characters in length.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.policy_document">
<code class="sig-name descname">policy_document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>The content of the policy. The content must be 1 to 2,048 characters in length.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.Policy.policy_type">
<code class="sig-name descname">policy_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the policy. Valid values: <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the policy was created.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the policy. Default to v1.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy. The description must be 1 to 1,024 characters in length.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the policy. The content must be 1 to 2,048 characters in length.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the policy. Valid values: <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">PolicyVersion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Policy Version resource. 
For information about Resource Manager Policy Version and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/116817.htm">What is Resource Manager Policy Version</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.84.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example_policy</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;examplePolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_name</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">,</span>
    <span class="n">policy_document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;         {</span>
<span class="s2">                        &quot;Statement&quot;: [{</span>
<span class="s2">                                &quot;Action&quot;: [&quot;oss:*&quot;],</span>
<span class="s2">                                &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                                &quot;Resource&quot;: [&quot;acs:oss:*:*:*&quot;]</span>
<span class="s2">                        }],</span>
<span class="s2">                        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">                }</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">example_policy_version</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">PolicyVersion</span><span class="p">(</span><span class="s2">&quot;examplePolicyVersion&quot;</span><span class="p">,</span>
    <span class="n">policy_name</span><span class="o">=</span><span class="n">example_policy</span><span class="o">.</span><span class="n">policy_name</span><span class="p">,</span>
    <span class="n">policy_document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;         {</span>
<span class="s2">                        &quot;Statement&quot;: [{</span>
<span class="s2">                                &quot;Action&quot;: [&quot;oss:*&quot;],</span>
<span class="s2">                                &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                                &quot;Resource&quot;: [&quot;acs:oss:*:*:myphotos&quot;]</span>
<span class="s2">                        }],</span>
<span class="s2">                        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">                }</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>is_default_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to set the policy version as the default version. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the policy. The content must be 1 to 2,048 characters in length.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.create_date">
<code class="sig-name descname">create_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the policy version was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.is_default_version">
<code class="sig-name descname">is_default_version</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.is_default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to set the policy version as the default version. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.policy_document">
<code class="sig-name descname">policy_document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>The content of the policy. The content must be 1 to 2,048 characters in length.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.version_id">
<code class="sig-name descname">version_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the policy version was created.</p></li>
<li><p><strong>is_default_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to set the policy version as the default version. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the policy. The content must be 1 to 2,048 characters in length.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the policy version.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.PolicyVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.PolicyVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">ResourceDirectory</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Manager Resource Directory resource. Resource Directory enables you to establish an organizational structure for the resources used by applications of your enterprise. You can plan, build, and manage the resources in a centralized manner by using only one resource directory.</p>
<p>For information about Resource Manager Resource Directory and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/en/doc-detail/94475.htm">What is Resource Manager Resource Directory</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.84.0+.</p>
<p><strong>NOTE:</strong> An account can only be used to enable a resource directory after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.</p>
<p><strong>NOTE:</strong> Before you destroy the resource, make sure that the following requirements are met:</p>
<ul class="simple">
<li><p>All member accounts must be removed from the resource directory.</p></li>
<li><p>All folders except the root folder must be deleted from the resource directory.</p></li>
</ul>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">ResourceDirectory</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.master_account_id">
<code class="sig-name descname">master_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.master_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the master account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.master_account_name">
<code class="sig-name descname">master_account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.master_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the master account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.root_folder_id">
<code class="sig-name descname">root_folder_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.root_folder_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the root folder.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_folder_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceDirectory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>master_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the master account.</p></li>
<li><p><strong>master_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the master account.</p></li>
<li><p><strong>root_folder_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the root folder.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.resourcemanager.ResourceDirectory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.ResourceDirectory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the resource group.The identifier must be 3 to 12 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (<a href="#id19"><span class="problematic" id="id20">*</span></a>). The identifier must start with a letter.</p></li>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the resource group.The identifier must be 3 to 12 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (<a href="#id23"><span class="problematic" id="id24">*</span></a>). The identifier must start with a letter.</p></li>
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

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_accounts">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_accounts</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Accounts of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_accounts</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstAccountId&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">accounts</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>ids</strong> (<em>list</em>) – A list of account IDs.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_folders">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_folders</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_folder_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_folders" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the resource manager folders of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.84.0+.</p>
<p><strong>NOTE:</strong>  You can view only the information of the first-level child folders of the specified folder.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_folders</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstFolderId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">folders</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of resource manager folders IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by folder name.</p></li>
<li><p><strong>parent_folder_id</strong> (<em>str</em>) – The ID of the parent folder.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_handshakes">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_handshakes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_handshakes" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Handshakes of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_handshakes</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstHandshakeId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">handshakes</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>ids</strong> (<em>list</em>) – A list of Resource Manager Handshake IDs.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_policies">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_policies</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Policies of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_policies</span><span class="p">(</span><span class="n">description_regex</span><span class="o">=</span><span class="s2">&quot;tftest_policy&quot;</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">,</span>
    <span class="n">policy_type</span><span class="o">=</span><span class="s2">&quot;Custom&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstPolicyId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">policies</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of Resource Manager Policy IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by policy name.</p></li>
<li><p><strong>policy_type</strong> (<em>str</em>) – The type of the policy. If you do not specify this parameter, the system lists all types of policies. Valid values: <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_policy_versions">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_policy_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_policy_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Policy Versions of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.85.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_policy_versions</span><span class="p">(</span><span class="n">policy_name</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">,</span>
    <span class="n">policy_type</span><span class="o">=</span><span class="s2">&quot;Custom&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstPolicyVersionId&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of policy version IDs.</p></li>
<li><p><strong>policy_name</strong> (<em>str</em>) – The name of the policy.</p></li>
<li><p><strong>policy_type</strong> (<em>str</em>) – The type of the policy. Valid values:<cite>Custom</cite> and <code class="docutils literal notranslate"><span class="pre">System</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_resource_directories">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_resource_directories</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_resource_directories" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Resource Directories of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">defaule</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_resource_directories</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;resourceDirectoryId&quot;</span><span class="p">,</span> <span class="n">defaule</span><span class="o">.</span><span class="n">directories</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_resource_groups">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_resource_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_resource_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides resource groups of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.84.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_resource_groups</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstResourceGroupId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">groups</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of resource group IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by resource group name.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the resource group. Possible values:<cite>Creating</cite>,<code class="docutils literal notranslate"><span class="pre">Deleted</span></code>,<code class="docutils literal notranslate"><span class="pre">OK</span></code> and <code class="docutils literal notranslate"><span class="pre">PendingDelete</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.resourcemanager.get_roles">
<code class="sig-prename descclassname">pulumi_alicloud.resourcemanager.</code><code class="sig-name descname">get_roles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.resourcemanager.get_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Resource Manager Roles of the current Alibaba Cloud user.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">resourcemanager</span><span class="o">.</span><span class="n">get_roles</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstRoleId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">roles</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of Resource Manager Role IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by role name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
