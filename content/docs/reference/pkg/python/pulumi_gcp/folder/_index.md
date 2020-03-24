---
title: Module folder
title_tag: Module folder | Package pulumi_gcp | Python SDK
linktitle: folder
notitle: true
---

<div class="section" id="folder">
<h1>folder<a class="headerlink" href="#folder" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.folder"></span><dl class="class">
<dt id="pulumi_gcp.folder.AwaitableGetOrganizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">AwaitableGetOrganizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">boolean_policies=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">list_policies=None</em>, <em class="sig-param">restore_policies=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.AwaitableGetOrganizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.folder.GetOrganizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">GetOrganizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">boolean_policies=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">list_policies=None</em>, <em class="sig-param">restore_policies=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.GetOrganizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganizationPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.folder.GetOrganizationPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.GetOrganizationPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.folder.IAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">IAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> This resource <em>must not</em> be used in conjunction with</dt><dd><p><code class="docutils literal notranslate"><span class="pre">folder.IAMPolicy</span></code> or they will fight over what your policy
should be.</p>
</dd>
<dt><strong>Note:</strong> On create, this resource will overwrite members of any existing roles.</dt><dd><p>Use <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">import</span></code> and inspect the output to ensure
your existing members are preserved.</p>
</dd>
</dl>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of identities that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
Each entry can have one of the following values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="o">**</span><span class="n">user</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">associated</span> <span class="k">with</span> <span class="n">a</span> <span class="n">specific</span> <span class="n">Google</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">alice</span><span class="nd">@gmail</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">serviceAccount</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">service</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">my</span><span class="o">-</span><span class="n">other</span><span class="o">-</span><span class="n">app</span><span class="nd">@appspot</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">group</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">Google</span> <span class="n">group</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">admins</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">domain</span><span class="p">:{</span><span class="n">domain</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">A</span> <span class="n">G</span> <span class="n">Suite</span> <span class="n">domain</span> <span class="p">(</span><span class="n">primary</span><span class="p">,</span> <span class="n">instead</span> <span class="n">of</span> <span class="n">alias</span><span class="p">)</span> <span class="n">name</span> <span class="n">that</span> <span class="n">represents</span> <span class="nb">all</span> <span class="n">the</span> <span class="n">users</span> <span class="n">of</span> <span class="n">that</span> <span class="n">domain</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">google</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="n">For</span> <span class="n">more</span> <span class="n">details</span> <span class="n">on</span> <span class="nb">format</span> <span class="ow">and</span> <span class="n">restrictions</span> <span class="n">see</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">cloud</span><span class="o">.</span><span class="n">google</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">billing</span><span class="o">/</span><span class="n">reference</span><span class="o">/</span><span class="n">rest</span><span class="o">/</span><span class="n">v1</span><span class="o">/</span><span class="n">Policy</span><span class="c1">#Binding</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">folder.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.members" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of identities that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
Each entry can have one of the following values:</p>
<ul class="simple">
<li><p><strong>user:{emailid}</strong>: An email address that is associated with a specific Google account. For example, <a class="reference external" href="mailto:alice&#37;&#52;&#48;gmail&#46;com">alice<span>&#64;</span>gmail<span>&#46;</span>com</a>.</p></li>
<li><p><strong>serviceAccount:{emailid}</strong>: An email address that represents a service account. For example, <a class="reference external" href="mailto:my-other-app&#37;&#52;&#48;appspot&#46;gserviceaccount&#46;com">my-other-app<span>&#64;</span>appspot<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a>.</p></li>
<li><p><strong>group:{emailid}</strong>: An email address that represents a Google group. For example, <a class="reference external" href="mailto:admins&#37;&#52;&#48;example&#46;com">admins<span>&#64;</span>example<span>&#46;</span>com</a>.</p></li>
<li><p><strong>domain:{domain}</strong>: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.</p></li>
<li><p>For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">folder.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the folder’s IAM policy.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of identities that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
Each entry can have one of the following values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="o">**</span><span class="n">user</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">associated</span> <span class="k">with</span> <span class="n">a</span> <span class="n">specific</span> <span class="n">Google</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">alice</span><span class="nd">@gmail</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">serviceAccount</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">service</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">my</span><span class="o">-</span><span class="n">other</span><span class="o">-</span><span class="n">app</span><span class="nd">@appspot</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">group</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">Google</span> <span class="n">group</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">admins</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">domain</span><span class="p">:{</span><span class="n">domain</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">A</span> <span class="n">G</span> <span class="n">Suite</span> <span class="n">domain</span> <span class="p">(</span><span class="n">primary</span><span class="p">,</span> <span class="n">instead</span> <span class="n">of</span> <span class="n">alias</span><span class="p">)</span> <span class="n">name</span> <span class="n">that</span> <span class="n">represents</span> <span class="nb">all</span> <span class="n">the</span> <span class="n">users</span> <span class="n">of</span> <span class="n">that</span> <span class="n">domain</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">google</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="n">For</span> <span class="n">more</span> <span class="n">details</span> <span class="n">on</span> <span class="nb">format</span> <span class="ow">and</span> <span class="n">restrictions</span> <span class="n">see</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">cloud</span><span class="o">.</span><span class="n">google</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">billing</span><span class="o">/</span><span class="n">reference</span><span class="o">/</span><span class="n">rest</span><span class="o">/</span><span class="n">v1</span><span class="o">/</span><span class="n">Policy</span><span class="c1">#Binding</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">folder.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">IAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> This resource <em>must not</em> be used in conjunction with</dt><dd><p><code class="docutils literal notranslate"><span class="pre">folder.IAMPolicy</span></code> or they will fight over what your policy
should be. Similarly, roles controlled by <code class="docutils literal notranslate"><span class="pre">folder.IAMBinding</span></code>
should not be assigned to using <code class="docutils literal notranslate"><span class="pre">folder.IAMMember</span></code>.</p>
</dd>
</dl>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a>
This field can have one of the following values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="o">**</span><span class="n">user</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">specific</span> <span class="n">Google</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">alice</span><span class="nd">@gmail</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">joe</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">serviceAccount</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">service</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">my</span><span class="o">-</span><span class="n">other</span><span class="o">-</span><span class="n">app</span><span class="nd">@appspot</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">group</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">Google</span> <span class="n">group</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">admins</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">domain</span><span class="p">:{</span><span class="n">domain</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">A</span> <span class="n">G</span> <span class="n">Suite</span> <span class="n">domain</span> <span class="p">(</span><span class="n">primary</span><span class="p">,</span> <span class="n">instead</span> <span class="n">of</span> <span class="n">alias</span><span class="p">)</span> <span class="n">name</span> <span class="n">that</span> <span class="n">represents</span> <span class="nb">all</span> <span class="n">the</span> <span class="n">users</span> <span class="n">of</span> <span class="n">that</span> <span class="n">domain</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">google</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.member">
<code class="sig-name descname">member</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.member" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a>
This field can have one of the following values:</p>
<ul class="simple">
<li><p><strong>user:{emailid}</strong>: An email address that represents a specific Google account. For example, <a class="reference external" href="mailto:alice&#37;&#52;&#48;gmail&#46;com">alice<span>&#64;</span>gmail<span>&#46;</span>com</a> or <a class="reference external" href="mailto:joe&#37;&#52;&#48;example&#46;com">joe<span>&#64;</span>example<span>&#46;</span>com</a>.</p></li>
<li><p><strong>serviceAccount:{emailid}</strong>: An email address that represents a service account. For example, <a class="reference external" href="mailto:my-other-app&#37;&#52;&#48;appspot&#46;gserviceaccount&#46;com">my-other-app<span>&#64;</span>appspot<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a>.</p></li>
<li><p><strong>group:{emailid}</strong>: An email address that represents a Google group. For example, <a class="reference external" href="mailto:admins&#37;&#52;&#48;example&#46;com">admins<span>&#64;</span>example<span>&#46;</span>com</a>.</p></li>
<li><p><strong>domain:{domain}</strong>: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the folder’s IAM policy.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a>
This field can have one of the following values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="o">**</span><span class="n">user</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">specific</span> <span class="n">Google</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">alice</span><span class="nd">@gmail</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">joe</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">serviceAccount</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">service</span> <span class="n">account</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">my</span><span class="o">-</span><span class="n">other</span><span class="o">-</span><span class="n">app</span><span class="nd">@appspot</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">group</span><span class="p">:{</span><span class="n">emailid</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">An</span> <span class="n">email</span> <span class="n">address</span> <span class="n">that</span> <span class="n">represents</span> <span class="n">a</span> <span class="n">Google</span> <span class="n">group</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">admins</span><span class="nd">@example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
<span class="o">*</span> <span class="o">**</span><span class="n">domain</span><span class="p">:{</span><span class="n">domain</span><span class="p">}</span><span class="o">**</span><span class="p">:</span> <span class="n">A</span> <span class="n">G</span> <span class="n">Suite</span> <span class="n">domain</span> <span class="p">(</span><span class="n">primary</span><span class="p">,</span> <span class="n">instead</span> <span class="n">of</span> <span class="n">alias</span><span class="p">)</span> <span class="n">name</span> <span class="n">that</span> <span class="n">represents</span> <span class="nb">all</span> <span class="n">the</span> <span class="n">users</span> <span class="n">of</span> <span class="n">that</span> <span class="n">domain</span><span class="o">.</span> <span class="n">For</span> <span class="n">example</span><span class="p">,</span> <span class="n">google</span><span class="o">.</span><span class="n">com</span> <span class="ow">or</span> <span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">IAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of the IAM policy for an existing Google Cloud
Platform folder.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">policy_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the folder’s IAM policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.OrganizationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">OrganizationPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">boolean_policy=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">list_policy=None</em>, <em class="sig-param">restore_policy=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Folder. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/folders/setOrgPolicy">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_organization_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p></li>
<li><p><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</p></li>
<li><p><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.</p></li>
<li><p><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boolean_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>list_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>restore_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.boolean_policy">
<code class="sig-name descname">boolean_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.boolean_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.constraint">
<code class="sig-name descname">constraint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.constraint" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.list_policy">
<code class="sig-name descname">list_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.list_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.restore_policy">
<code class="sig-name descname">restore_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.restore_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A restore policy is a constraint to restore the default policy. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the Policy. Default version is 0.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.OrganizationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">boolean_policy=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">list_policy=None</em>, <em class="sig-param">restore_policy=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p></li>
<li><p><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</p></li>
<li><p><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.</p></li>
<li><p><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boolean_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>list_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>restore_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.OrganizationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.OrganizationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.get_organization_policy">
<code class="sig-prename descclassname">pulumi_gcp.folder.</code><code class="sig-name descname">get_organization_policy</code><span class="sig-paren">(</span><em class="sig-param">constraint=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.get_organization_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Folder. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_folder_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_folder_organization_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>constraint</strong> (<em>str</em>) – <p>(Required) The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</p></li>
<li><p><strong>folder</strong> (<em>str</em>) – The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
