---
---

<div class="section" id="iam">
<h1>iam<a class="headerlink" href="#iam" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp/issues">terraform-providers/terraform-provider-gcp repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.iam"></span><dl class="class">
<dt id="pulumi_gcp.iam.GetRuleResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.iam.</code><code class="descname">GetRuleResult</code><span class="sig-paren">(</span><em>included_permissions=None</em>, <em>name=None</em>, <em>stage=None</em>, <em>title=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.included_permissions">
<code class="descname">included_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.included_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>specifies the list of one or more permissions to include in the custom role, such as - <code class="docutils literal notranslate"><span class="pre">iam.roles.get</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.stage">
<code class="descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>indicates the stage of a role in the launch lifecycle, such as <code class="docutils literal notranslate"><span class="pre">GA</span></code>, <code class="docutils literal notranslate"><span class="pre">BETA</span></code> or <code class="docutils literal notranslate"><span class="pre">ALPHA</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.title">
<code class="descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.title" title="Permalink to this definition">¶</a></dt>
<dd><p>is a friendly title for the role, such as “Role Viewer”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.iam.get_rule">
<code class="descclassname">pulumi_gcp.iam.</code><code class="descname">get_rule</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google IAM Role.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/iam_role.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/iam_role.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
