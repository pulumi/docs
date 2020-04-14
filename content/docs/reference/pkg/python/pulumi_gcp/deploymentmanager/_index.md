---
title: Module deploymentmanager
title_tag: Module deploymentmanager | Package pulumi_gcp | Python SDK
linktitle: deploymentmanager
notitle: true
---

<div class="section" id="deploymentmanager">
<h1>deploymentmanager<a class="headerlink" href="#deploymentmanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.deploymentmanager"></span><dl class="class">
<dt id="pulumi_gcp.deploymentmanager.Deployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.deploymentmanager.</code><code class="sig-name descname">Deployment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_policy=None</em>, <em class="sig-param">delete_policy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preview=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of resources that are deployed and managed together using
a configuration file</p>
<blockquote>
<div><p><strong>Warning:</strong> This resource is intended only to manage a Deployment resource,
and attempts to manage the Deployment’s resources in the provider as well
will likely result in errors or unexpected behavior as the two tools
fight over ownership. We strongly discourage doing so unless you are an
experienced user of both tools.</p>
</div></blockquote>
<p>In addition, due to limitations of the API, the provider will treat
deployments in preview as recreate-only for any update operation other
than actually deploying an in-preview deployment (i.e. <code class="docutils literal notranslate"><span class="pre">preview=true</span></code> to
<code class="docutils literal notranslate"><span class="pre">preview=false</span></code>).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/deployment_manager_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/deployment_manager_deployment.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the policy to use for creating new resources. Only used on create and update. Valid values are ‘CREATE_OR_ACQUIRE’
(default) or ‘ACQUIRE’. If set to ‘ACQUIRE’ and resources do not already exist, the deployment will fail. Note that
updating this field does not actually affect the deployment, just how it is updated.</p></li>
<li><p><strong>delete_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the policy to use for deleting new resources on update/delete. Valid values are ‘DELETE’ (default) or ‘ABANDON’. If
‘DELETE’, resource is deleted after removal from Deployment Manager. If ‘ABANDON’, the resource is only removed from
Deployment Manager and is not actually deleted. Note that updating this field does not actually change the deployment,
just how it is updated.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional user-provided description of deployment.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Key-value pairs to apply to this labels.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name for the deployment</p></li>
<li><p><strong>preview</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, a deployment is created with “shell” resources that are not actually instantiated. This allows you to
preview a deployment. It can be updated to false to actually deploy with real resources. ~&gt;<strong>NOTE</strong>: Deployment Manager
does not allow update of a deployment in preview (unless updating to preview=false). Thus, Terraform will force-recreate
deployments if either preview is updated to true or if other fields are updated while preview is true.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters that define your deployment, including the deployment configuration and relevant templates.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.create_policy">
<code class="sig-name descname">create_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.create_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the policy to use for creating new resources. Only used on create and update. Valid values are ‘CREATE_OR_ACQUIRE’
(default) or ‘ACQUIRE’. If set to ‘ACQUIRE’ and resources do not already exist, the deployment will fail. Note that
updating this field does not actually affect the deployment, just how it is updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.delete_policy">
<code class="sig-name descname">delete_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.delete_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the policy to use for deleting new resources on update/delete. Valid values are ‘DELETE’ (default) or ‘ABANDON’. If
‘DELETE’, resource is deleted after removal from Deployment Manager. If ‘ABANDON’, the resource is only removed from
Deployment Manager and is not actually deleted. Note that updating this field does not actually change the deployment,
just how it is updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for deployment. Output only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional user-provided description of deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value pairs to apply to this labels.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.manifest">
<code class="sig-name descname">manifest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.manifest" title="Permalink to this definition">¶</a></dt>
<dd><p>Output only. URL of the manifest representing the last manifest that was successfully deployed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name for the deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.preview">
<code class="sig-name descname">preview</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.preview" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, a deployment is created with “shell” resources that are not actually instantiated. This allows you to
preview a deployment. It can be updated to false to actually deploy with real resources. ~&gt;<strong>NOTE</strong>: Deployment Manager
does not allow update of a deployment in preview (unless updating to preview=false). Thus, Terraform will force-recreate
deployments if either preview is updated to true or if other fields are updated while preview is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>Output only. Server defined URL for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.deploymentmanager.Deployment.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.target" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters that define your deployment, including the deployment configuration and relevant templates.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imports</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.deploymentmanager.Deployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_policy=None</em>, <em class="sig-param">delete_policy=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">manifest=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preview=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Deployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the policy to use for creating new resources. Only used on create and update. Valid values are ‘CREATE_OR_ACQUIRE’
(default) or ‘ACQUIRE’. If set to ‘ACQUIRE’ and resources do not already exist, the deployment will fail. Note that
updating this field does not actually affect the deployment, just how it is updated.</p></li>
<li><p><strong>delete_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the policy to use for deleting new resources on update/delete. Valid values are ‘DELETE’ (default) or ‘ABANDON’. If
‘DELETE’, resource is deleted after removal from Deployment Manager. If ‘ABANDON’, the resource is only removed from
Deployment Manager and is not actually deleted. Note that updating this field does not actually change the deployment,
just how it is updated.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for deployment. Output only.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional user-provided description of deployment.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Key-value pairs to apply to this labels.</p></li>
<li><p><strong>manifest</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Output only. URL of the manifest representing the last manifest that was successfully deployed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name for the deployment</p></li>
<li><p><strong>preview</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, a deployment is created with “shell” resources that are not actually instantiated. This allows you to
preview a deployment. It can be updated to false to actually deploy with real resources. ~&gt;<strong>NOTE</strong>: Deployment Manager
does not allow update of a deployment in preview (unless updating to preview=false). Thus, Terraform will force-recreate
deployments if either preview is updated to true or if other fields are updated while preview is true.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Output only. Server defined URL for the resource.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters that define your deployment, including the deployment configuration and relevant templates.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.deploymentmanager.Deployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.deploymentmanager.Deployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.deploymentmanager.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
