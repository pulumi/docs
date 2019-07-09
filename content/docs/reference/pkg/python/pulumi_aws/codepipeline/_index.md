---
---

<div class="section" id="module-pulumi_aws.codepipeline">
<span id="codepipeline"></span><h1>codepipeline<a class="headerlink" href="#module-pulumi_aws.codepipeline" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.codepipeline.Pipeline">
<em class="property">class </em><code class="descclassname">pulumi_aws.codepipeline.</code><code class="descname">Pipeline</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>artifact_store=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>stages=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodePipeline.</p>
<blockquote>
<div><strong>NOTE on ``aws_codepipeline``:</strong> - the <code class="docutils literal notranslate"><span class="pre">GITHUB_TOKEN</span></code> environment variable must be set if the GitHub provider is specified.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>artifact_store</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An artifact_store block. Artifact stores are documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codepipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codepipeline.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The codepipeline ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.artifact_store">
<code class="descname">artifact_store</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.artifact_store" title="Permalink to this definition">¶</a></dt>
<dd><p>An artifact_store block. Artifact stores are documented below.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">stage</span></code> (Minimum of at least two <code class="docutils literal notranslate"><span class="pre">stage</span></code> blocks is required) A stage block. Stages are documented below.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codepipeline.Pipeline.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codepipeline.Pipeline.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.codepipeline.Webhook">
<em class="property">class </em><code class="descclassname">pulumi_aws.codepipeline.</code><code class="descname">Webhook</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>authentication=None</em>, <em>authentication_configuration=None</em>, <em>filters=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>target_action=None</em>, <em>target_pipeline=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodePipeline Webhook.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authentication  to use. One of <code class="docutils literal notranslate"><span class="pre">IP</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNAUTHENTICATED</span></code>.</li>
<li><strong>authentication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>. Auth blocks are documented below.</li>
<li><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks. Filter blocks are documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</li>
<li><strong>target_pipeline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codepipeline_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codepipeline_webhook.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.authentication">
<code class="descname">authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authentication  to use. One of <code class="docutils literal notranslate"><span class="pre">IP</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNAUTHENTICATED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.authentication_configuration">
<code class="descname">authentication_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.authentication_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>. Auth blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.filters">
<code class="descname">filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks. Filter blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.target_action">
<code class="descname">target_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.target_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.target_pipeline">
<code class="descname">target_pipeline</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.target_pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codepipeline.Webhook.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodePipeline webhook’s URL. POST events to this endpoint to trigger the target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codepipeline.Webhook.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codepipeline.Webhook.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
