<div class="section" id="module-pulumi_gcp.iam">
<span id="iam"></span><h1>iam<a class="headerlink" href="#module-pulumi_gcp.iam" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.iam.GetRuleResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.iam.</code><code class="descname">GetRuleResult</code><span class="sig-paren">(</span><em>included_permissions=None</em>, <em>stage=None</em>, <em>title=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.included_permissions">
<code class="descname">included_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.included_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>specifies the list of one or more permissions to include in the custom role, such as - <cite>iam.roles.get</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iam.GetRuleResult.stage">
<code class="descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iam.GetRuleResult.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>indicates the stage of a role in the launch lifecycle, such as <cite>GA</cite>, <cite>BETA</cite> or <cite>ALPHA</cite>.</p>
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
<code class="descclassname">pulumi_gcp.iam.</code><code class="descname">get_rule</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iam.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Google IAM Role.</p>
<p><a href="#id1"><span class="problematic" id="id2">``</span></a><a href="#id3"><span class="problematic" id="id4">`</span></a>hcl
data “google_iam_role” “roleinfo” {</p>
<blockquote>
<div>name = “roles/compute.viewer”</div></blockquote>
<p>}</p>
<dl class="docutils">
<dt>output “the_role_permissions” {</dt>
<dd>value = “${data.google_iam_role.roleinfo.included_permissions}”</dd>
</dl>
<p>}</p>
<p><a href="#id5"><span class="problematic" id="id6">``</span></a><a href="#id7"><span class="problematic" id="id8">`</span></a></p>
</dd></dl>

</div>
