---
title: Module iam
title_tag: Module iam | Package pulumi_gcp | Python SDK
linktitle: iam
notitle: true
---

<div class="section" id="iam">
<h1>iam<a class="headerlink" href="#iam" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.iam"></span><dl class="py class">
<dt id="pulumi_gcp.iam.AwaitableGetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">AwaitableGetRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">included_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.AwaitableGetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.iam.AwaitableGetTestablePermissionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">AwaitableGetTestablePermissionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">custom_support_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_resource_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.AwaitableGetTestablePermissionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.iam.GetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">GetRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">included_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.included_permissions">
<code class="sig-name descname">included_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.included_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>specifies the list of one or more permissions to include in the custom role, such as - <code class="docutils literal notranslate"><span class="pre">iam.roles.get</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.stage">
<code class="sig-name descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>indicates the stage of a role in the launch lifecycle, such as <code class="docutils literal notranslate"><span class="pre">GA</span></code>, <code class="docutils literal notranslate"><span class="pre">BETA</span></code> or <code class="docutils literal notranslate"><span class="pre">ALPHA</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.title" title="Permalink to this definition">¶</a></dt>
<dd><p>is a friendly title for the role, such as “Role Viewer”</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.iam.GetTestablePermissionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">GetTestablePermissionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">custom_support_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_resource_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.GetTestablePermissionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTestablePermissions.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetTestablePermissionsResult.custom_support_level">
<code class="sig-name descname">custom_support_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetTestablePermissionsResult.custom_support_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The the support level of this permission for custom roles.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetTestablePermissionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetTestablePermissionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iam.GetTestablePermissionsResult.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetTestablePermissionsResult.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of permissions matching the provided input. Structure is defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.iam.get_rule">
<code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">get_rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google IAM Role.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">roleinfo</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">get_rule</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;roles/compute.viewer&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;theRolePermissions&quot;</span><span class="p">,</span> <span class="n">roleinfo</span><span class="o">.</span><span class="n">included_permissions</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the Role to lookup in the form <code class="docutils literal notranslate"><span class="pre">roles/{ROLE_NAME}</span></code>, <code class="docutils literal notranslate"><span class="pre">organizations/{ORGANIZATION_ID}/roles/{ROLE_NAME}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/roles/{ROLE_NAME}</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.iam.get_testable_permissions">
<code class="sig-prename descclassname">pulumi_gcp.iam.</code><code class="sig-name descname">get_testable_permissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">custom_support_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_resource_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.get_testable_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve a list of testable permissions for a resource. Testable permissions mean the permissions that user can add or remove in a role at a given resource. The resource can be referenced either via the full resource name or via a URI.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">perms</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">get_testable_permissions</span><span class="p">(</span><span class="n">full_resource_name</span><span class="o">=</span><span class="s2">&quot;//cloudresourcemanager.googleapis.com/projects/my-project&quot;</span><span class="p">,</span>
    <span class="n">stages</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;GA&quot;</span><span class="p">,</span>
        <span class="s2">&quot;BETA&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>custom_support_level</strong> (<em>str</em>) – The level of support for custom roles. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;NOT_SUPPORTED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUPPORTED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TESTING&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;SUPPORTED&quot;</span></code></p></li>
<li><p><strong>full_resource_name</strong> (<em>str</em>) – See <a class="reference external" href="https://cloud.google.com/apis/design/resource_names#full_resource_name">full resource name documentation</a> for more detail.</p></li>
<li><p><strong>stages</strong> (<em>list</em>) – The acceptable release stages of the permission in the output. Note that <code class="docutils literal notranslate"><span class="pre">BETA</span></code> does not include permissions in <code class="docutils literal notranslate"><span class="pre">GA</span></code>, but you can specify both with <code class="docutils literal notranslate"><span class="pre">[&quot;GA&quot;,</span> <span class="pre">&quot;BETA&quot;]</span></code> for example. Can be a list of <code class="docutils literal notranslate"><span class="pre">&quot;ALPHA&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;BETA&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GA&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;DEPRECATED&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">[&quot;GA&quot;]</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
