---
title: Module billing
title_tag: Module billing | Package pulumi_gcp | Python SDK
linktitle: billing
notitle: true
---

<div class="section" id="billing">
<h1>billing<a class="headerlink" href="#billing" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.billing"></span><dl class="py class">
<dt id="pulumi_gcp.billing.AccountIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.billing.</code><code class="sig-name descname">AccountIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Billing Account.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt><dd><p><code class="docutils literal notranslate"><span class="pre">billing.AccountIamMember</span></code> for the <strong>same role</strong> or they will fight over
what your policy should be.</p>
</dd>
<dt><strong>Note:</strong> On create, this resource will overwrite members of any existing roles.</dt><dd><p>Use <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">import</span></code> and inspect the output to ensure
your existing members are preserved.</p>
</dd>
</dl>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">billing</span><span class="o">.</span><span class="n">AccountIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">billing_account_id</span><span class="o">=</span><span class="s2">&quot;00AA00-000AAA-00AA0A&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:alice@gmail.com&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/billing.viewer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.billing_account_id">
<code class="sig-name descname">billing_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the billing account’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.members">
<code class="sig-name descname">members</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the billing account’s IAM policy.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.AccountIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.AccountIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.billing.</code><code class="sig-name descname">AccountIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Billing Account.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt><dd><p><code class="docutils literal notranslate"><span class="pre">billing.AccountIamBinding</span></code> for the <strong>same role</strong> or they will fight over
what your policy should be.</p>
</dd>
</dl>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">billing</span><span class="o">.</span><span class="n">AccountIamMember</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">billing_account_id</span><span class="o">=</span><span class="s2">&quot;00AA00-000AAA-00AA0A&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:alice@gmail.com&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/billing.viewer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.billing_account_id">
<code class="sig-name descname">billing_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the billing account’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.member">
<code class="sig-name descname">member</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.member" title="Permalink to this definition">¶</a></dt>
<dd><p>The user that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the billing account’s IAM policy.</p></li>
<li><p><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user that the role should apply to. For more details on format and restrictions see <a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/Policy#Binding">https://cloud.google.com/billing/reference/rest/v1/Policy#Binding</a></p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.AccountIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.AccountIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.billing.</code><code class="sig-name descname">AccountIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of the entire IAM policy for an existing Google Cloud Platform Billing Account.</p>
<blockquote>
<div><p><strong>Warning:</strong> Billing accounts have a default user that can be <strong>overwritten</strong>
by use of this resource. The safest alternative is to use multiple <code class="docutils literal notranslate"><span class="pre">billing.AccountIamBinding</span></code></p>
<blockquote>
<div><p>resources. If you do use this resource, the best way to be sure that you are
not making dangerous changes is to start by importing your existing policy,
and examining the diff very closely.</p>
</div></blockquote>
<dl class="simple">
<dt><strong>Note:</strong> This resource <strong>must not</strong> be used in conjunction with</dt><dd><p><code class="docutils literal notranslate"><span class="pre">billing.AccountIamMember</span></code> or <code class="docutils literal notranslate"><span class="pre">billing.AccountIamBinding</span></code>
or they will fight over what your policy should be.</p>
</dd>
</dl>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/billing.viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">billing</span><span class="o">.</span><span class="n">AccountIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">billing_account_id</span><span class="o">=</span><span class="s2">&quot;00AA00-000AAA-00AA0A&quot;</span><span class="p">,</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamPolicy.billing_account_id">
<code class="sig-name descname">billing_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.billing_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.AccountIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account id.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.AccountIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.AccountIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.AccountIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.Budget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.billing.</code><code class="sig-name descname">Budget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">all_updates_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">budget_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.Budget" title="Permalink to this definition">¶</a></dt>
<dd><p>Budget configuration for a billing account.</p>
<p>To get more information about Budget, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/billing/docs/reference/budget/rest/v1beta1/billingAccounts.budgets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/billing/docs/how-to/budgets">Creating a budget</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">account</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_billing_account</span><span class="p">(</span><span class="n">billing_account</span><span class="o">=</span><span class="s2">&quot;000000-0000000-0000000-000000&quot;</span><span class="p">)</span>
<span class="n">budget</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">billing</span><span class="o">.</span><span class="n">Budget</span><span class="p">(</span><span class="s2">&quot;budget&quot;</span><span class="p">,</span>
    <span class="n">billing_account</span><span class="o">=</span><span class="n">account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Example Billing Budget&quot;</span><span class="p">,</span>
    <span class="n">amount</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;specified_amount&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;currencyCode&quot;</span><span class="p">:</span> <span class="s2">&quot;USD&quot;</span><span class="p">,</span>
            <span class="s2">&quot;units&quot;</span><span class="p">:</span> <span class="s2">&quot;100000&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">threshold_rules</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;thresholdPercent&quot;</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">account</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_billing_account</span><span class="p">(</span><span class="n">billing_account</span><span class="o">=</span><span class="s2">&quot;000000-0000000-0000000-000000&quot;</span><span class="p">)</span>
<span class="n">budget</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">billing</span><span class="o">.</span><span class="n">Budget</span><span class="p">(</span><span class="s2">&quot;budget&quot;</span><span class="p">,</span>
    <span class="n">billing_account</span><span class="o">=</span><span class="n">account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Example Billing Budget&quot;</span><span class="p">,</span>
    <span class="n">budget_filter</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;projects&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;projects/my-project-name&quot;</span><span class="p">],</span>
        <span class="s2">&quot;creditTypesTreatment&quot;</span><span class="p">:</span> <span class="s2">&quot;EXCLUDE_ALL_CREDITS&quot;</span><span class="p">,</span>
        <span class="s2">&quot;services&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;services/24E6-581D-38E5&quot;</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="n">amount</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;specified_amount&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;currencyCode&quot;</span><span class="p">:</span> <span class="s2">&quot;USD&quot;</span><span class="p">,</span>
            <span class="s2">&quot;units&quot;</span><span class="p">:</span> <span class="s2">&quot;100000&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">threshold_rules</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;thresholdPercent&quot;</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;thresholdPercent&quot;</span><span class="p">:</span> <span class="mf">0.9</span><span class="p">,</span>
            <span class="s2">&quot;spendBasis&quot;</span><span class="p">:</span> <span class="s2">&quot;FORECASTED_SPEND&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_updates_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines notifications that are sent on every update to the
billing account’s spend, regardless of the thresholds defined
using threshold rules.  Structure is documented below.</p></li>
<li><p><strong>amount</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The budgeted amount for each usage period.  Structure is documented below.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the billing account to set a budget on.</p></li>
<li><p><strong>budget_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Filters that define which resources are used to compute the actual
spend against the budget.  Structure is documented below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User data for display name in UI. Must be &lt;= 60 chars.</p></li>
<li><p><strong>threshold_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules that trigger alerts (notifications of thresholds being
crossed) when spend exceeds the specified percentages of the
budget.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>all_updates_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Cloud Pub/Sub topic where budget related
messages will be published, in the form
projects/{project_id}/topics/{topic_id}. Updates are sent
at regular intervals to the topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The schema version of the notification. Only “1.0” is
accepted. It represents the JSON schema as defined in
<a class="reference external" href="https://cloud.google.com/billing/docs/how-to/budgets#notification_format">https://cloud.google.com/billing/docs/how-to/budgets#notification_format</a>.</p></li>
</ul>
<p>The <strong>amount</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">specifiedAmount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A specified amount to use as the budget. currencyCode is
optional. If specified, it must match the currency of the
billing account. The currencyCode is provided on output.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">currencyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The 3-letter currency code defined in ISO 4217.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of nano (10^-9) units of the amount.
The value must be between -999,999,999 and +999,999,999
inclusive. If units is positive, nanos must be positive or
zero. If units is zero, nanos can be positive, zero, or
negative. If units is negative, nanos must be negative or
zero. For example $-1.75 is represented as units=-1 and
nanos=-750,000,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The whole units of the amount. For example if currencyCode
is “USD”, then 1 unit is one US dollar.</p></li>
</ul>
</li>
</ul>
<p>The <strong>budget_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creditTypesTreatment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how credits should be treated when determining spend
for threshold calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of projects of the form projects/{project_id},
specifying that usage from only this set of projects should be
included in the budget. If omitted, the report will include
all usage for the billing account, regardless of which project
the usage occurred on. Only zero or one project can be
specified currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">services</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of services of the form services/{service_id},
specifying that usage from only this set of services should be
included in the budget. If omitted, the report will include
usage for all the services. The service names are available
through the Catalog API:
<a class="reference external" href="https://cloud.google.com/billing/v1/how-tos/catalog-api">https://cloud.google.com/billing/v1/how-tos/catalog-api</a>.</p></li>
</ul>
<p>The <strong>threshold_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spendBasis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of basis used to determine if spend has passed
the threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdPercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Send an alert when this threshold is exceeded. This is a
1.0-based percentage, so 0.5 = 50%. Must be &gt;= 0.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.all_updates_rule">
<code class="sig-name descname">all_updates_rule</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.all_updates_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines notifications that are sent on every update to the
billing account’s spend, regardless of the thresholds defined
using threshold rules.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Cloud Pub/Sub topic where budget related
messages will be published, in the form
projects/{project_id}/topics/{topic_id}. Updates are sent
at regular intervals to the topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The schema version of the notification. Only “1.0” is
accepted. It represents the JSON schema as defined in
<a class="reference external" href="https://cloud.google.com/billing/docs/how-to/budgets#notification_format">https://cloud.google.com/billing/docs/how-to/budgets#notification_format</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.amount">
<code class="sig-name descname">amount</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.amount" title="Permalink to this definition">¶</a></dt>
<dd><p>The budgeted amount for each usage period.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">specifiedAmount</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A specified amount to use as the budget. currencyCode is
optional. If specified, it must match the currency of the
billing account. The currencyCode is provided on output.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">currencyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The 3-letter currency code defined in ISO 4217.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanos</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of nano (10^-9) units of the amount.
The value must be between -999,999,999 and +999,999,999
inclusive. If units is positive, nanos must be positive or
zero. If units is zero, nanos can be positive, zero, or
negative. If units is negative, nanos must be negative or
zero. For example $-1.75 is represented as units=-1 and
nanos=-750,000,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The whole units of the amount. For example if currencyCode
is “USD”, then 1 unit is one US dollar.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.billing_account">
<code class="sig-name descname">billing_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the billing account to set a budget on.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.budget_filter">
<code class="sig-name descname">budget_filter</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.budget_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Filters that define which resources are used to compute the actual
spend against the budget.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creditTypesTreatment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how credits should be treated when determining spend
for threshold calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of projects of the form projects/{project_id},
specifying that usage from only this set of projects should be
included in the budget. If omitted, the report will include
all usage for the billing account, regardless of which project
the usage occurred on. Only zero or one project can be
specified currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">services</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of services of the form services/{service_id},
specifying that usage from only this set of services should be
included in the budget. If omitted, the report will include
usage for all the services. The service names are available
through the Catalog API:
<a class="reference external" href="https://cloud.google.com/billing/v1/how-tos/catalog-api">https://cloud.google.com/billing/v1/how-tos/catalog-api</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User data for display name in UI. Must be &lt;= 60 chars.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name of the budget. The resource name implies the scope of a budget. Values are of the form
billingAccounts/{billingAccountId}/budgets/{budgetId}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.billing.Budget.threshold_rules">
<code class="sig-name descname">threshold_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.billing.Budget.threshold_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rules that trigger alerts (notifications of thresholds being
crossed) when spend exceeds the specified percentages of the
budget.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spendBasis</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of basis used to determine if spend has passed
the threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdPercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Send an alert when this threshold is exceeded. This is a
1.0-based percentage, so 0.5 = 50%. Must be &gt;= 0.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.Budget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">all_updates_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">budget_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.Budget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Budget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_updates_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines notifications that are sent on every update to the
billing account’s spend, regardless of the thresholds defined
using threshold rules.  Structure is documented below.</p></li>
<li><p><strong>amount</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The budgeted amount for each usage period.  Structure is documented below.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the billing account to set a budget on.</p></li>
<li><p><strong>budget_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Filters that define which resources are used to compute the actual
spend against the budget.  Structure is documented below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User data for display name in UI. Must be &lt;= 60 chars.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name of the budget. The resource name implies the scope of a budget. Values are of the form
billingAccounts/{billingAccountId}/budgets/{budgetId}.</p></li>
<li><p><strong>threshold_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules that trigger alerts (notifications of thresholds being
crossed) when spend exceeds the specified percentages of the
budget.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>all_updates_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Cloud Pub/Sub topic where budget related
messages will be published, in the form
projects/{project_id}/topics/{topic_id}. Updates are sent
at regular intervals to the topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The schema version of the notification. Only “1.0” is
accepted. It represents the JSON schema as defined in
<a class="reference external" href="https://cloud.google.com/billing/docs/how-to/budgets#notification_format">https://cloud.google.com/billing/docs/how-to/budgets#notification_format</a>.</p></li>
</ul>
<p>The <strong>amount</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">specifiedAmount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A specified amount to use as the budget. currencyCode is
optional. If specified, it must match the currency of the
billing account. The currencyCode is provided on output.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">currencyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The 3-letter currency code defined in ISO 4217.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of nano (10^-9) units of the amount.
The value must be between -999,999,999 and +999,999,999
inclusive. If units is positive, nanos must be positive or
zero. If units is zero, nanos can be positive, zero, or
negative. If units is negative, nanos must be negative or
zero. For example $-1.75 is represented as units=-1 and
nanos=-750,000,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The whole units of the amount. For example if currencyCode
is “USD”, then 1 unit is one US dollar.</p></li>
</ul>
</li>
</ul>
<p>The <strong>budget_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creditTypesTreatment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how credits should be treated when determining spend
for threshold calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of projects of the form projects/{project_id},
specifying that usage from only this set of projects should be
included in the budget. If omitted, the report will include
all usage for the billing account, regardless of which project
the usage occurred on. Only zero or one project can be
specified currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">services</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of services of the form services/{service_id},
specifying that usage from only this set of services should be
included in the budget. If omitted, the report will include
usage for all the services. The service names are available
through the Catalog API:
<a class="reference external" href="https://cloud.google.com/billing/v1/how-tos/catalog-api">https://cloud.google.com/billing/v1/how-tos/catalog-api</a>.</p></li>
</ul>
<p>The <strong>threshold_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spendBasis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of basis used to determine if spend has passed
the threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdPercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Send an alert when this threshold is exceeded. This is a
1.0-based percentage, so 0.5 = 50%. Must be &gt;= 0.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.billing.Budget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.Budget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.billing.Budget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.billing.Budget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
