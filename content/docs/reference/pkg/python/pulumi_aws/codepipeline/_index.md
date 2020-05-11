---
title: Module codepipeline
title_tag: Module codepipeline | Package pulumi_aws | Python SDK
linktitle: codepipeline
notitle: true
---

<div class="section" id="codepipeline">
<h1>codepipeline<a class="headerlink" href="#codepipeline" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codepipeline"></span><dl class="py class">
<dt id="pulumi_aws.codepipeline.Pipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codepipeline.</code><code class="sig-name descname">Pipeline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">artifact_store</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodePipeline.</p>
<blockquote>
<div><p><strong>NOTE on ``codepipeline.Pipeline``:</strong> - the <code class="docutils literal notranslate"><span class="pre">GITHUB_TOKEN</span></code> environment variable must be set if the GitHub provider is specified.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">codepipeline_bucket</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;codepipelineBucket&quot;</span><span class="p">,</span> <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
<span class="n">codepipeline_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;codepipelineRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: {</span>
<span class="s2">        &quot;Service&quot;: &quot;codepipeline.amazonaws.com&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;Action&quot;: &quot;sts:AssumeRole&quot;</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">codepipeline_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicy</span><span class="p">(</span><span class="s2">&quot;codepipelinePolicy&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">codepipeline_bucket</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span> <span class="n">codepipeline_bucket</span><span class="o">.</span><span class="n">arn</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">codepipelineBucketArn</span><span class="p">,</span> <span class="n">codepipelineBucketArn1</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">  &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">      &quot;Effect&quot;:&quot;Allow&quot;,</span>
<span class="s2">      &quot;Action&quot;: [</span>
<span class="s2">        &quot;s3:GetObject&quot;,</span>
<span class="s2">        &quot;s3:GetObjectVersion&quot;,</span>
<span class="s2">        &quot;s3:GetBucketVersioning&quot;,</span>
<span class="s2">        &quot;s3:PutObject&quot;</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Resource&quot;: [</span>
<span class="s2">        &quot;</span><span class="si">{</span><span class="n">codepipeline_bucket_arn</span><span class="si">}</span><span class="s2">&quot;,</span>
<span class="s2">        &quot;</span><span class="si">{</span><span class="n">codepipeline_bucket_arn1</span><span class="si">}</span><span class="s2">/*&quot;</span>
<span class="s2">      ]</span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">    </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Action&quot;: [</span>
<span class="s2">        &quot;codebuild:BatchGetBuilds&quot;,</span>
<span class="s2">        &quot;codebuild:StartBuild&quot;</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Resource&quot;: &quot;*&quot;</span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">  ]</span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">),</span>
    <span class="n">role</span><span class="o">=</span><span class="n">codepipeline_role</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">s3kmskey</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_alias</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;alias/myKmsKey&quot;</span><span class="p">)</span>
<span class="n">codepipeline</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">codepipeline</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">(</span><span class="s2">&quot;codepipeline&quot;</span><span class="p">,</span>
    <span class="n">artifact_store</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;encryptionKey&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;id&quot;</span><span class="p">:</span> <span class="n">s3kmskey</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;KMS&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="n">codepipeline_bucket</span><span class="o">.</span><span class="n">bucket</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;S3&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="n">codepipeline_role</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
    <span class="n">stages</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
                <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;Branch&quot;</span><span class="p">:</span> <span class="s2">&quot;master&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;Owner&quot;</span><span class="p">:</span> <span class="s2">&quot;my-organization&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;Repo&quot;</span><span class="p">:</span> <span class="s2">&quot;test&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
                <span class="s2">&quot;outputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;source_output&quot;</span><span class="p">],</span>
                <span class="s2">&quot;owner&quot;</span><span class="p">:</span> <span class="s2">&quot;ThirdParty&quot;</span><span class="p">,</span>
                <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="s2">&quot;GitHub&quot;</span><span class="p">,</span>
                <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
                <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;ProjectName&quot;</span><span class="p">:</span> <span class="s2">&quot;test&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;inputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;source_output&quot;</span><span class="p">],</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
                <span class="s2">&quot;outputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;build_output&quot;</span><span class="p">],</span>
                <span class="s2">&quot;owner&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
                <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="s2">&quot;CodeBuild&quot;</span><span class="p">,</span>
                <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Deploy&quot;</span><span class="p">,</span>
                <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;ActionMode&quot;</span><span class="p">:</span> <span class="s2">&quot;REPLACE_ON_FAILURE&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;Capabilities&quot;</span><span class="p">:</span> <span class="s2">&quot;CAPABILITY_AUTO_EXPAND,CAPABILITY_IAM&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;OutputFileName&quot;</span><span class="p">:</span> <span class="s2">&quot;CreateStackOutput.json&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;StackName&quot;</span><span class="p">:</span> <span class="s2">&quot;MyStack&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;TemplatePath&quot;</span><span class="p">:</span> <span class="s2">&quot;build_output::sam-templated.yaml&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;inputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;build_output&quot;</span><span class="p">],</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Deploy&quot;</span><span class="p">,</span>
                <span class="s2">&quot;owner&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
                <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="s2">&quot;CloudFormation&quot;</span><span class="p">,</span>
                <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Deploy&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>artifact_store</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more artifact_store blocks. Artifact stores are documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.</p></li>
<li><p><strong>stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A stage block. Stages are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>artifact_store</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don’t specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An <code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> block is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KMS key ARN or ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of key; currently only <code class="docutils literal notranslate"><span class="pre">KMS</span></code> is supported</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location where AWS CodePipeline stores artifacts for a pipeline; currently only <code class="docutils literal notranslate"><span class="pre">S3</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the artifact store, such as Amazon S3</p></li>
</ul>
<p>The <strong>stages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The action(s) to include in the stage. Defined as an <code class="docutils literal notranslate"><span class="pre">action</span></code> block below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are <code class="docutils literal notranslate"><span class="pre">Approval</span></code>, <code class="docutils literal notranslate"><span class="pre">Build</span></code>, <code class="docutils literal notranslate"><span class="pre">Deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">Invoke</span></code>, <code class="docutils literal notranslate"><span class="pre">Source</span></code> and <code class="docutils literal notranslate"><span class="pre">Test</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A Map of the action declaration’s configuration. Find out more about configuring action configurations in the <a class="reference external" href="http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements">Reference Pipeline Structure documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of artifact names to be worked on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action declaration’s name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace all output variables will be accessed from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of artifact names to output. Output artifact names must be unique within a pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The creator of the action being called. Possible values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">ThirdParty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region in which to run the action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order in which actions are run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string that identifies the action type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the stage.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The codepipeline ARN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.artifact_store">
<code class="sig-name descname">artifact_store</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.artifact_store" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more artifact_store blocks. Artifact stores are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don’t specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An <code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> block is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The KMS key ARN or ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of key; currently only <code class="docutils literal notranslate"><span class="pre">KMS</span></code> is supported</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location where AWS CodePipeline stores artifacts for a pipeline; currently only <code class="docutils literal notranslate"><span class="pre">S3</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the artifact store, such as Amazon S3</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.stages">
<code class="sig-name descname">stages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.stages" title="Permalink to this definition">¶</a></dt>
<dd><p>A stage block. Stages are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The action(s) to include in the stage. Defined as an <code class="docutils literal notranslate"><span class="pre">action</span></code> block below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are <code class="docutils literal notranslate"><span class="pre">Approval</span></code>, <code class="docutils literal notranslate"><span class="pre">Build</span></code>, <code class="docutils literal notranslate"><span class="pre">Deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">Invoke</span></code>, <code class="docutils literal notranslate"><span class="pre">Source</span></code> and <code class="docutils literal notranslate"><span class="pre">Test</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A Map of the action declaration’s configuration. Find out more about configuring action configurations in the <a class="reference external" href="http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements">Reference Pipeline Structure documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of artifact names to be worked on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action declaration’s name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace all output variables will be accessed from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of artifact names to output. Output artifact names must be unique within a pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The creator of the action being called. Possible values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">ThirdParty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region in which to run the action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The order in which actions are run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string that identifies the action type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the stage.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Pipeline.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codepipeline.Pipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">artifact_store</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The codepipeline ARN.</p></li>
<li><p><strong>artifact_store</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more artifact_store blocks. Artifact stores are documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.</p></li>
<li><p><strong>stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A stage block. Stages are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>artifact_store</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don’t specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An <code class="docutils literal notranslate"><span class="pre">encryption_key</span></code> block is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KMS key ARN or ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of key; currently only <code class="docutils literal notranslate"><span class="pre">KMS</span></code> is supported</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location where AWS CodePipeline stores artifacts for a pipeline; currently only <code class="docutils literal notranslate"><span class="pre">S3</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the artifact store, such as Amazon S3</p></li>
</ul>
<p>The <strong>stages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The action(s) to include in the stage. Defined as an <code class="docutils literal notranslate"><span class="pre">action</span></code> block below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are <code class="docutils literal notranslate"><span class="pre">Approval</span></code>, <code class="docutils literal notranslate"><span class="pre">Build</span></code>, <code class="docutils literal notranslate"><span class="pre">Deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">Invoke</span></code>, <code class="docutils literal notranslate"><span class="pre">Source</span></code> and <code class="docutils literal notranslate"><span class="pre">Test</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A Map of the action declaration’s configuration. Find out more about configuring action configurations in the <a class="reference external" href="http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements">Reference Pipeline Structure documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of artifact names to be worked on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action declaration’s name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace all output variables will be accessed from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputArtifacts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of artifact names to output. Output artifact names must be unique within a pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The creator of the action being called. Possible values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code> and <code class="docutils literal notranslate"><span class="pre">ThirdParty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region in which to run the action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order in which actions are run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string that identifies the action type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the stage.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codepipeline.Pipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codepipeline.Pipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codepipeline.Webhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codepipeline.</code><code class="sig-name descname">Webhook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_pipeline</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodePipeline Webhook.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">bar_pipeline</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">codepipeline</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">(</span><span class="s2">&quot;barPipeline&quot;</span><span class="p">,</span>
    <span class="n">artifact_store</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;encryptionKey&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;id&quot;</span><span class="p">:</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;kms.Alias&quot;</span><span class="p">][</span><span class="s2">&quot;s3kmskey&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;KMS&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="n">aws_s3_bucket</span><span class="p">[</span><span class="s2">&quot;bar&quot;</span><span class="p">][</span><span class="s2">&quot;bucket&quot;</span><span class="p">],</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;S3&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;bar&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">stages</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
                <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;Branch&quot;</span><span class="p">:</span> <span class="s2">&quot;master&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;Owner&quot;</span><span class="p">:</span> <span class="s2">&quot;my-organization&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;Repo&quot;</span><span class="p">:</span> <span class="s2">&quot;test&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
                <span class="s2">&quot;outputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">],</span>
                <span class="s2">&quot;owner&quot;</span><span class="p">:</span> <span class="s2">&quot;ThirdParty&quot;</span><span class="p">,</span>
                <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="s2">&quot;GitHub&quot;</span><span class="p">,</span>
                <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Source&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
                <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;ProjectName&quot;</span><span class="p">:</span> <span class="s2">&quot;test&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;inputArtifacts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">],</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
                <span class="s2">&quot;owner&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
                <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="s2">&quot;CodeBuild&quot;</span><span class="p">,</span>
                <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Build&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
<span class="n">webhook_secret</span> <span class="o">=</span> <span class="s2">&quot;super-secret&quot;</span>
<span class="n">bar_webhook</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">codepipeline</span><span class="o">.</span><span class="n">Webhook</span><span class="p">(</span><span class="s2">&quot;barWebhook&quot;</span><span class="p">,</span>
    <span class="n">authentication</span><span class="o">=</span><span class="s2">&quot;GITHUB_HMAC&quot;</span><span class="p">,</span>
    <span class="n">authentication_configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;secretToken&quot;</span><span class="p">:</span> <span class="n">webhook_secret</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;jsonPath&quot;</span><span class="p">:</span> <span class="s2">&quot;$$.ref&quot;</span><span class="p">,</span>
        <span class="s2">&quot;matchEquals&quot;</span><span class="p">:</span> <span class="s2">&quot;refs/heads/</span><span class="si">{Branch}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">target_action</span><span class="o">=</span><span class="s2">&quot;Source&quot;</span><span class="p">,</span>
    <span class="n">target_pipeline</span><span class="o">=</span><span class="n">bar_pipeline</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="c1"># Wire the CodePipeline webhook into a GitHub repository.</span>
<span class="n">bar_repository_webhook</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryWebhook</span><span class="p">(</span><span class="s2">&quot;barRepositoryWebhook&quot;</span><span class="p">,</span>
    <span class="n">configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;contentType&quot;</span><span class="p">:</span> <span class="s2">&quot;json&quot;</span><span class="p">,</span>
        <span class="s2">&quot;insecureSsl&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;secret&quot;</span><span class="p">:</span> <span class="n">webhook_secret</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="n">bar_webhook</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">events</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;push&quot;</span><span class="p">],</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">github_repository</span><span class="p">[</span><span class="s2">&quot;repo&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authentication  to use. One of <code class="docutils literal notranslate"><span class="pre">IP</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNAUTHENTICATED</span></code>.</p></li>
<li><p><strong>authentication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>. Auth blocks are documented below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks. Filter blocks are documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>target_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</p></li>
<li><p><strong>target_pipeline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedIpRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A valid CIDR block for <code class="docutils literal notranslate"><span class="pre">IP</span></code> filtering. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The shared secret for the GitHub repository webhook. Set this as <code class="docutils literal notranslate"><span class="pre">secret</span></code> in your <code class="docutils literal notranslate"><span class="pre">github_repository_webhook</span></code>’s <code class="docutils literal notranslate"><span class="pre">configuration</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>.</p></li>
</ul>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <a class="reference external" href="https://github.com/json-path/JsonPath">JSON path</a> to filter on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to match on (e.g. <code class="docutils literal notranslate"><span class="pre">refs/heads/{Branch}</span></code>). See <a class="reference external" href="https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html">AWS docs</a> for details.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.authentication">
<code class="sig-name descname">authentication</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authentication  to use. One of <code class="docutils literal notranslate"><span class="pre">IP</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNAUTHENTICATED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.authentication_configuration">
<code class="sig-name descname">authentication_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.authentication_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>. Auth blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedIpRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A valid CIDR block for <code class="docutils literal notranslate"><span class="pre">IP</span></code> filtering. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The shared secret for the GitHub repository webhook. Set this as <code class="docutils literal notranslate"><span class="pre">secret</span></code> in your <code class="docutils literal notranslate"><span class="pre">github_repository_webhook</span></code>’s <code class="docutils literal notranslate"><span class="pre">configuration</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.filters">
<code class="sig-name descname">filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks. Filter blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <a class="reference external" href="https://github.com/json-path/JsonPath">JSON path</a> to filter on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to match on (e.g. <code class="docutils literal notranslate"><span class="pre">refs/heads/{Branch}</span></code>). See <a class="reference external" href="https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html">AWS docs</a> for details.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.target_action">
<code class="sig-name descname">target_action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.target_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.target_pipeline">
<code class="sig-name descname">target_pipeline</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.target_pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codepipeline.Webhook.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodePipeline webhook’s URL. POST events to this endpoint to trigger the target.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codepipeline.Webhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_pipeline</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Webhook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authentication  to use. One of <code class="docutils literal notranslate"><span class="pre">IP</span></code>, <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNAUTHENTICATED</span></code>.</p></li>
<li><p><strong>authentication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>. Auth blocks are documented below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks. Filter blocks are documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>target_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.</p></li>
<li><p><strong>target_pipeline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CodePipeline webhook’s URL. POST events to this endpoint to trigger the target.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedIpRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A valid CIDR block for <code class="docutils literal notranslate"><span class="pre">IP</span></code> filtering. Required for <code class="docutils literal notranslate"><span class="pre">IP</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The shared secret for the GitHub repository webhook. Set this as <code class="docutils literal notranslate"><span class="pre">secret</span></code> in your <code class="docutils literal notranslate"><span class="pre">github_repository_webhook</span></code>’s <code class="docutils literal notranslate"><span class="pre">configuration</span></code> block. Required for <code class="docutils literal notranslate"><span class="pre">GITHUB_HMAC</span></code>.</p></li>
</ul>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jsonPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <a class="reference external" href="https://github.com/json-path/JsonPath">JSON path</a> to filter on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to match on (e.g. <code class="docutils literal notranslate"><span class="pre">refs/heads/{Branch}</span></code>). See <a class="reference external" href="https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html">AWS docs</a> for details.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codepipeline.Webhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codepipeline.Webhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codepipeline.Webhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
