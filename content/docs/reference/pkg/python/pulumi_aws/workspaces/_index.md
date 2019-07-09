---
---

<div class="section" id="workspaces">
<h1>workspaces<a class="headerlink" href="#workspaces" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.workspaces"></span><dl class="class">
<dt id="pulumi_aws.workspaces.GetBundleResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.workspaces.</code><code class="descname">GetBundleResult</code><span class="sig-paren">(</span><em>bundle_id=None</em>, <em>compute_types=None</em>, <em>description=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>root_storages=None</em>, <em>user_storages=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBundle.</p>
<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.compute_types">
<code class="descname">compute_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.compute_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute type. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the compute type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.root_storages">
<code class="descname">root_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.root_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The root volume. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.user_storages">
<code class="descname">user_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.user_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The user storage. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.workspaces.get_bundle">
<code class="descclassname">pulumi_aws.workspaces.</code><code class="descname">get_bundle</code><span class="sig-paren">(</span><em>bundle_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.get_bundle" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Workspaces Bundle.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/workspaces_bundle.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/workspaces_bundle.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
