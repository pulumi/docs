---
title: Module workspaces
title_tag: Module workspaces | Package pulumi_aws | Python SDK
linktitle: workspaces
notitle: true
---

<div class="section" id="workspaces">
<h1>workspaces<a class="headerlink" href="#workspaces" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.workspaces"></span><dl class="class">
<dt id="pulumi_aws.workspaces.AwaitableGetBundleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">AwaitableGetBundleResult</code><span class="sig-paren">(</span><em class="sig-param">bundle_id=None</em>, <em class="sig-param">compute_types=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">root_storages=None</em>, <em class="sig-param">user_storages=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.AwaitableGetBundleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.workspaces.GetBundleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">GetBundleResult</code><span class="sig-paren">(</span><em class="sig-param">bundle_id=None</em>, <em class="sig-param">compute_types=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">root_storages=None</em>, <em class="sig-param">user_storages=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBundle.</p>
<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.compute_types">
<code class="sig-name descname">compute_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.compute_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute type. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the compute type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.root_storages">
<code class="sig-name descname">root_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.root_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The root volume. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.user_storages">
<code class="sig-name descname">user_storages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.user_storages" title="Permalink to this definition">¶</a></dt>
<dd><p>The user storage. See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.workspaces.GetBundleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.workspaces.GetBundleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.workspaces.get_bundle">
<code class="sig-prename descclassname">pulumi_aws.workspaces.</code><code class="sig-name descname">get_bundle</code><span class="sig-paren">(</span><em class="sig-param">bundle_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.workspaces.get_bundle" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Workspaces Bundle.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>bundle_id</strong> (<em>str</em>) – The ID of the bundle.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/workspaces_bundle.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/workspaces_bundle.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
