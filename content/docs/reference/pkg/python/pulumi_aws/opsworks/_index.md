---
title: Module opsworks
title_tag: Module opsworks | Package pulumi_aws | Python SDK
linktitle: opsworks
notitle: true
---

<div class="section" id="opsworks">
<h1>opsworks<a class="headerlink" href="#opsworks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.opsworks"></span><dl class="py class">
<dt id="pulumi_aws.opsworks.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_bundle_on_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_flow_ruby_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_root</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rails_env</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks application resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo_app</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;foo-app&quot;</span><span class="p">,</span>
    <span class="n">app_sources</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;revision&quot;</span><span class="p">:</span> <span class="s2">&quot;master&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;git&quot;</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;https://github.com/example.git&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">auto_bundle_on_deploy</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This is a Rails application&quot;</span><span class="p">,</span>
    <span class="n">document_root</span><span class="o">=</span><span class="s2">&quot;public&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sub.example.com&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">enable_ssl</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">environments</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;key&quot;</span><span class="p">,</span>
        <span class="s2">&quot;secure&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">rails_env</span><span class="o">=</span><span class="s2">&quot;staging&quot;</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">ssl_configurations</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;certificate&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./foobar.crt&quot;</span><span class="p">),</span>
        <span class="s2">&quot;privateKey&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./foobar.key&quot;</span><span class="p">),</span>
    <span class="p">}],</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;rails&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SCM configuration of the app as described below.</p></li>
<li><p><strong>auto_bundle_on_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>aws_flow_ruby_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify activity and workflow workers for your app using the aws-flow gem.</p></li>
<li><p><strong>data_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s ARN.</p></li>
<li><p><strong>data_source_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database name.</p></li>
<li><p><strong>data_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the app.</p></li>
<li><p><strong>document_root</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual host alias.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p></li>
<li><p><strong>environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object to define environment variables.  Object is described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the application.</p></li>
<li><p><strong>rails_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p></li>
<li><p><strong>ssl_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The SSL configuration of the app. Object is described below.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the application will belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Opsworks application type. One of <code class="docutils literal notranslate"><span class="pre">aws-flow-ruby</span></code>, <code class="docutils literal notranslate"><span class="pre">java</span></code>, <code class="docutils literal notranslate"><span class="pre">rails</span></code>, <code class="docutils literal notranslate"><span class="pre">php</span></code>, <code class="docutils literal notranslate"><span class="pre">nodejs</span></code>, <code class="docutils literal notranslate"><span class="pre">static</span></code> or <code class="docutils literal notranslate"><span class="pre">other</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SSH key to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
<p>The <strong>environments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set visibility of the variable value to <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable value.</p></li>
</ul>
<p>The <strong>ssl_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The contents of the certificate’s domain.crt file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be used to specify an intermediate certificate authority key or client authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private key; the contents of the certificate’s domain.key file.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.app_sources">
<code class="sig-name descname">app_sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.app_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>SCM configuration of the app as described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Password to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SSH key to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.auto_bundle_on_deploy">
<code class="sig-name descname">auto_bundle_on_deploy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.auto_bundle_on_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.aws_flow_ruby_settings">
<code class="sig-name descname">aws_flow_ruby_settings</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.aws_flow_ruby_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify activity and workflow workers for your app using the aws-flow gem.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_arn">
<code class="sig-name descname">data_source_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s ARN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_database_name">
<code class="sig-name descname">data_source_database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The database name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_type">
<code class="sig-name descname">data_source_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.document_root">
<code class="sig-name descname">document_root</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.document_root" title="Permalink to this definition">¶</a></dt>
<dd><p>Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.domains">
<code class="sig-name descname">domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of virtual host alias.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.enable_ssl">
<code class="sig-name descname">enable_ssl</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.enable_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.environments">
<code class="sig-name descname">environments</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Object to define environment variables.  Object is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Variable name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set visibility of the variable value to <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Variable value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.rails_env">
<code class="sig-name descname">rails_env</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.rails_env" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.short_name">
<code class="sig-name descname">short_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.ssl_configurations">
<code class="sig-name descname">ssl_configurations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.ssl_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL configuration of the app. Object is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The contents of the certificate’s domain.crt file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Can be used to specify an intermediate certificate authority key or client authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private key; the contents of the certificate’s domain.key file.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the application will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Application.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Opsworks application type. One of <code class="docutils literal notranslate"><span class="pre">aws-flow-ruby</span></code>, <code class="docutils literal notranslate"><span class="pre">java</span></code>, <code class="docutils literal notranslate"><span class="pre">rails</span></code>, <code class="docutils literal notranslate"><span class="pre">php</span></code>, <code class="docutils literal notranslate"><span class="pre">nodejs</span></code>, <code class="docutils literal notranslate"><span class="pre">static</span></code> or <code class="docutils literal notranslate"><span class="pre">other</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_bundle_on_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_flow_ruby_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_root</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rails_env</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SCM configuration of the app as described below.</p></li>
<li><p><strong>auto_bundle_on_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Run bundle install when deploying for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>aws_flow_ruby_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify activity and workflow workers for your app using the aws-flow gem.</p></li>
<li><p><strong>data_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s ARN.</p></li>
<li><p><strong>data_source_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database name.</p></li>
<li><p><strong>data_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s type one of <code class="docutils literal notranslate"><span class="pre">AutoSelectOpsworksMysqlInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OpsworksMysqlInstance</span></code>, or <code class="docutils literal notranslate"><span class="pre">RdsDbInstance</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the app.</p></li>
<li><p><strong>document_root</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subfolder for the document root for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual host alias.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable SSL for the app. This must be set in order to let <code class="docutils literal notranslate"><span class="pre">ssl_configuration.private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl_configuration.certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">ssl_configuration.chain</span></code> take effect.</p></li>
<li><p><strong>environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object to define environment variables.  Object is described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the application.</p></li>
<li><p><strong>rails_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rails environment for application of type <code class="docutils literal notranslate"><span class="pre">rails</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p></li>
<li><p><strong>ssl_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The SSL configuration of the app. Object is described below.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the application will belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Opsworks application type. One of <code class="docutils literal notranslate"><span class="pre">aws-flow-ruby</span></code>, <code class="docutils literal notranslate"><span class="pre">java</span></code>, <code class="docutils literal notranslate"><span class="pre">rails</span></code>, <code class="docutils literal notranslate"><span class="pre">php</span></code>, <code class="docutils literal notranslate"><span class="pre">nodejs</span></code>, <code class="docutils literal notranslate"><span class="pre">static</span></code> or <code class="docutils literal notranslate"><span class="pre">other</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SSH key to use when authenticating to the source. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the app resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
<p>The <strong>environments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set visibility of the variable value to <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable value.</p></li>
</ul>
<p>The <strong>ssl_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The contents of the certificate’s domain.crt file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be used to specify an intermediate certificate authority key or client authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private key; the contents of the certificate’s domain.key file.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.CustomLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">CustomLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks custom layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">custlayer</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">CustomLayer</span><span class="p">(</span><span class="s2">&quot;custlayer&quot;</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;awesome&quot;</span><span class="p">,</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Encrypt the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Encrypt the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.short_name">
<code class="sig-name descname">short_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.CustomLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Encrypt the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.CustomLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.CustomLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.GangliaLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">GangliaLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ganglia layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">monitor</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">GangliaLayer</span><span class="p">(</span><span class="s2">&quot;monitor&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;foobarbaz&quot;</span><span class="p">,</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for Ganglia.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to use for Ganglia. Defaults to “/ganglia”.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for Ganglia. Defaults to “opsworks”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for Ganglia.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to use for Ganglia. Defaults to “/ganglia”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username to use for Ganglia. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.GangliaLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GangliaLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for Ganglia.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to use for Ganglia. Defaults to “/ganglia”.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for Ganglia. Defaults to “opsworks”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.HaproxyLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">HaproxyLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks haproxy layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">lb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">HaproxyLayer</span><span class="p">(</span><span class="s2">&quot;lb&quot;</span><span class="p">,</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">stats_password</span><span class="o">=</span><span class="s2">&quot;foobarbaz&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>healthcheck_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p></li>
<li><p><strong>healthcheck_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL path to use for instance healthchecks. Defaults to “/”.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>stats_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable HAProxy stats.</p></li>
<li><p><strong>stats_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for HAProxy stats.</p></li>
<li><p><strong>stats_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HAProxy stats URL. Defaults to “/haproxy?stats”.</p></li>
<li><p><strong>stats_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for HAProxy stats. Defaults to “opsworks”.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_method">
<code class="sig-name descname">healthcheck_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_method" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_url">
<code class="sig-name descname">healthcheck_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL path to use for instance healthchecks. Defaults to “/”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_enabled">
<code class="sig-name descname">stats_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable HAProxy stats.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_password">
<code class="sig-name descname">stats_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for HAProxy stats.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_url">
<code class="sig-name descname">stats_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The HAProxy stats URL. Defaults to “/haproxy?stats”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_user">
<code class="sig-name descname">stats_user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The username for HAProxy stats. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stats_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HaproxyLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>healthcheck_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p></li>
<li><p><strong>healthcheck_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL path to use for instance healthchecks. Defaults to “/”.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>stats_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable HAProxy stats.</p></li>
<li><p><strong>stats_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use for HAProxy stats.</p></li>
<li><p><strong>stats_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HAProxy stats URL. Defaults to “/haproxy?stats”.</p></li>
<li><p><strong>stats_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for HAProxy stats. Defaults to “opsworks”.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_ebs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_cluster_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">infrastructure_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_service_error_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layer_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registered_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_host_dsa_key_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_host_rsa_key_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtualization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks instance resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">my_instance</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;my-instance&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;t2.micro&quot;</span><span class="p">,</span>
    <span class="n">layer_ids</span><span class="o">=</span><span class="p">[</span><span class="n">aws_opsworks_custom_layer</span><span class="p">[</span><span class="s2">&quot;my-layer&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">os</span><span class="o">=</span><span class="s2">&quot;Amazon Linux 2015.09&quot;</span><span class="p">,</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;stopped&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Each of the <code class="docutils literal notranslate"><span class="pre">*_block_device</span></code> attributes controls a portion of the AWS
Instance’s “Block Device Mapping”. It’s a good idea to familiarize yourself with <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">AWS’s Block Device
Mapping docs</a>
to understand the implications of using these attributes.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">root_block_device</span></code> mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> - (Optional) The type of volume. Can be <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;gp2&quot;</span></code>,
or <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> - (Optional) The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> - (Optional) The amount of provisioned
<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html">IOPS</a>.
This must be set with a <code class="docutils literal notranslate"><span class="pre">volume_type</span></code> of <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_on_termination</span></code> - (Optional) Whether the volume should be destroyed
on instance termination (Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
</ul>
<p>Modifying any of the <code class="docutils literal notranslate"><span class="pre">root_block_device</span></code> settings requires resource
replacement.</p>
<p>Each <code class="docutils literal notranslate"><span class="pre">ebs_block_device</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> - The name of the device to mount.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> - (Optional) The Snapshot ID to mount.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> - (Optional) The type of volume. Can be <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;gp2&quot;</span></code>,
or <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">&quot;standard&quot;</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> - (Optional) The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> - (Optional) The amount of provisioned
<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html">IOPS</a>.
This must be set with a <code class="docutils literal notranslate"><span class="pre">volume_type</span></code> of <code class="docutils literal notranslate"><span class="pre">&quot;io1&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_on_termination</span></code> - (Optional) Whether the volume should be destroyed
on instance termination (Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
</ul>
<p>Modifying any <code class="docutils literal notranslate"><span class="pre">ebs_block_device</span></code> currently requires resource replacement.</p>
<p>Each <code class="docutils literal notranslate"><span class="pre">ephemeral_block_device</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> - The name of the block device to mount on the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_name</span></code> - The <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames">Instance Store Device
Name</a>
(e.g. <code class="docutils literal notranslate"><span class="pre">&quot;ephemeral0&quot;</span></code>)</p></li>
</ul>
<p>Each AWS Instance type has a different set of Instance Store block devices
available for attachment. AWS <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes">publishes a
list</a>
of which ephemeral devices are available on each type. The devices are always
identified by the <code class="docutils literal notranslate"><span class="pre">virtual_name</span></code> in the format <code class="docutils literal notranslate"><span class="pre">&quot;ephemeral{0..N}&quot;</span></code>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Currently, changes to <code class="docutils literal notranslate"><span class="pre">*_block_device</span></code> configuration of <em>existing</em>
resources cannot be automatically detected by this provider. After making updates
to block device configuration, resource recreation can be manually triggered by
using the <cite>``up`</cite> command with the –replace argument &lt;<a class="reference external" href="https://www.pulumi.com/docs/reference/cli/pulumi_up/">https://www.pulumi.com/docs/reference/cli/pulumi_up/</a>&gt;`_.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p></li>
<li><p><strong>ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p></li>
<li><p><strong>auto_scaling_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default.</p></li>
<li><p><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</p></li>
<li><p><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance’s host name.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start</p></li>
<li><p><strong>layer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ids of the layers the instance will belong to.</p></li>
<li><p><strong>os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of operating system that will be installed.</p></li>
<li><p><strong>private_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address assigned to the instance</p></li>
<li><p><strong>public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address assigned to the instance, if applicable.</p></li>
<li><p><strong>root_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</p></li>
<li><p><strong>root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the instance will belong to.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to attach to</p></li>
<li><p><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p></li>
<li><p><strong>virtualization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>root_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.agent_version">
<code class="sig-name descname">agent_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ami_id">
<code class="sig-name descname">ami_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.architecture">
<code class="sig-name descname">architecture</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.auto_scaling_type">
<code class="sig-name descname">auto_scaling_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.auto_scaling_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_block_devices">
<code class="sig-name descname">ebs_block_devices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ec2_instance_id">
<code class="sig-name descname">ec2_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ec2_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 instance ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ephemeral_block_devices">
<code class="sig-name descname">ephemeral_block_devices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance’s host name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.layer_ids">
<code class="sig-name descname">layer_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.layer_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids of the layers the instance will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.os">
<code class="sig-name descname">os</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of operating system that will be installed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.private_dns">
<code class="sig-name descname">private_dns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address assigned to the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.public_dns">
<code class="sig-name descname">public_dns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.public_ip">
<code class="sig-name descname">public_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the instance, if applicable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.root_block_devices">
<code class="sig-name descname">root_block_devices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.root_device_type">
<code class="sig-name descname">root_device_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.ssh_key_name">
<code class="sig-name descname">ssh_key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the instance will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet ID to attach to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.tenancy">
<code class="sig-name descname">tenancy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Instance.virtualization_type">
<code class="sig-name descname">virtualization_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_ebs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ec2_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_cluster_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">infrastructure_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_service_error_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layer_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registered_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reported_os_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_host_dsa_key_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_host_rsa_key_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtualization_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS OpsWorks agent to install.  Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;INHERIT&quot;</span></code>.</p></li>
<li><p><strong>ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.  If an AMI is specified, <code class="docutils literal notranslate"><span class="pre">os</span></code> must be <code class="docutils literal notranslate"><span class="pre">&quot;Custom&quot;</span></code>.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;x86_64&quot;</span></code> (the default) or <code class="docutils literal notranslate"><span class="pre">&quot;i386&quot;</span></code></p></li>
<li><p><strong>auto_scaling_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates load-based or time-based instances.  If set, can be either: <code class="docutils literal notranslate"><span class="pre">&quot;load&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;timer&quot;</span></code>.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default.</p></li>
<li><p><strong>ebs_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</p></li>
<li><p><strong>ec2_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EC2 instance ID</p></li>
<li><p><strong>ephemeral_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance’s host name.</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls where to install OS and package updates when the instance boots.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start</p></li>
<li><p><strong>layer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ids of the layers the instance will belong to.</p></li>
<li><p><strong>os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of operating system that will be installed.</p></li>
<li><p><strong>private_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address assigned to the instance</p></li>
<li><p><strong>public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address assigned to the instance, if applicable.</p></li>
<li><p><strong>root_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize details about the root block
device of the instance. See Block Devices below for details.</p></li>
<li><p><strong>root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;ebs&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;instance-store&quot;</span></code></p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the instance will belong to.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired state of the instance.  Can be either <code class="docutils literal notranslate"><span class="pre">&quot;running&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;stopped&quot;</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet ID to attach to</p></li>
<li><p><strong>tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance tenancy to use. Can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;host&quot;</span></code></p></li>
<li><p><strong>virtualization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword to choose what virtualization mode created instances
will use. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;paravirtual&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;hvm&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>root_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.JavaAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">JavaAppLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Java application layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">JavaAppLayer</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the application container to use. Defaults to “tomcat”.</p></li>
<li><p><strong>app_server_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the selected application container to use. Defaults to “7”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>jvm_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Options to set for the JVM.</p></li>
<li><p><strong>jvm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p></li>
<li><p><strong>jvm_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of JVM to use. Defaults to “7”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server">
<code class="sig-name descname">app_server</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the application container to use. Defaults to “tomcat”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server_version">
<code class="sig-name descname">app_server_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the selected application container to use. Defaults to “7”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_options">
<code class="sig-name descname">jvm_options</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options to set for the JVM.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_type">
<code class="sig-name descname">jvm_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_version">
<code class="sig-name descname">jvm_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of JVM to use. Defaults to “7”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jvm_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JavaAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the application container to use. Defaults to “tomcat”.</p></li>
<li><p><strong>app_server_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the selected application container to use. Defaults to “7”.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>jvm_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Options to set for the JVM.</p></li>
<li><p><strong>jvm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the type of JVM to use. Defaults to <code class="docutils literal notranslate"><span class="pre">openjdk</span></code>.</p></li>
<li><p><strong>jvm_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of JVM to use. Defaults to “7”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MemcachedLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">MemcachedLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks memcached layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">MemcachedLayer</span><span class="p">(</span><span class="s2">&quot;cache&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.allocated_memory">
<code class="sig-name descname">allocated_memory</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.allocated_memory" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MemcachedLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MysqlLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">MysqlLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password_on_all_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks MySQL layer resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the root password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">MysqlLayer</span><span class="p">(</span><span class="s2">&quot;db&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to use for MySQL.</p></li>
<li><p><strong>root_password_on_all_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password">
<code class="sig-name descname">root_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to use for MySQL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances">
<code class="sig-name descname">root_password_on_all_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.MysqlLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password_on_all_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MysqlLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to use for MySQL.</p></li>
<li><p><strong>root_password_on_all_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.NodejsAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">NodejsAppLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodejs_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks NodeJS application layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">NodejsAppLayer</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>nodejs_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of NodeJS to use. Defaults to “0.10.38”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.nodejs_version">
<code class="sig-name descname">nodejs_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.nodejs_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of NodeJS to use. Defaults to “0.10.38”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodejs_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodejsAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>nodejs_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of NodeJS to use. Defaults to “0.10.38”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Permission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Permission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_sudo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks permission resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">my_stack_permission</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">Permission</span><span class="p">(</span><span class="s2">&quot;myStackPermission&quot;</span><span class="p">,</span>
    <span class="n">allow_ssh</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">allow_sudo</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">level</span><span class="o">=</span><span class="s2">&quot;iam_only&quot;</span><span class="p">,</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;stack&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">user_arn</span><span class="o">=</span><span class="n">aws_iam_user</span><span class="p">[</span><span class="s2">&quot;user&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use SSH to communicate with the instance</p></li>
<li><p><strong>allow_sudo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use sudo to elevate privileges</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to set the permissions for</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN to set permissions for</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_ssh">
<code class="sig-name descname">allow_ssh</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use SSH to communicate with the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_sudo">
<code class="sig-name descname">allow_sudo</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_sudo" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use sudo to elevate privileges</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Permission.level">
<code class="sig-name descname">level</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.level" title="Permalink to this definition">¶</a></dt>
<dd><p>The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Permission.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to set the permissions for</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Permission.user_arn">
<code class="sig-name descname">user_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN to set permissions for</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Permission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_sudo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Permission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use SSH to communicate with the instance</p></li>
<li><p><strong>allow_sudo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use sudo to elevate privileges</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users permission level. Mus be one of <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">show</span></code>, <code class="docutils literal notranslate"><span class="pre">deploy</span></code>, <code class="docutils literal notranslate"><span class="pre">manage</span></code>, <code class="docutils literal notranslate"><span class="pre">iam_only</span></code></p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to set the permissions for</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN to set permissions for</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Permission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Permission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.PhpAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">PhpAppLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks PHP application layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">PhpAppLayer</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PhpAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RailsAppLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">RailsAppLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bundler_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_bundler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passenger_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ruby_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rubygems_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ruby on Rails application layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">RailsAppLayer</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the app server to use. Defaults to “apache_passenger”.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>bundler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>manage_bundler</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether OpsWorks should manage bundler. On by default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>passenger_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Passenger to use. Defaults to “4.0.46”.</p></li>
<li><p><strong>ruby_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Ruby to use. Defaults to “2.0.0”.</p></li>
<li><p><strong>rubygems_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of RubyGems to use. Defaults to “2.2.2”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.app_server">
<code class="sig-name descname">app_server</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the app server to use. Defaults to “apache_passenger”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.bundler_version">
<code class="sig-name descname">bundler_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.bundler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.manage_bundler">
<code class="sig-name descname">manage_bundler</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.manage_bundler" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether OpsWorks should manage bundler. On by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.passenger_version">
<code class="sig-name descname">passenger_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.passenger_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Passenger to use. Defaults to “4.0.46”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ruby_version">
<code class="sig-name descname">ruby_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ruby_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Ruby to use. Defaults to “2.0.0”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.rubygems_version">
<code class="sig-name descname">rubygems_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.rubygems_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of RubyGems to use. Defaults to “2.2.2”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bundler_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_bundler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passenger_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ruby_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rubygems_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RailsAppLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the app server to use. Defaults to “apache_passenger”.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>bundler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the layer.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>manage_bundler</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether OpsWorks should manage bundler. On by default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>passenger_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Passenger to use. Defaults to “4.0.46”.</p></li>
<li><p><strong>ruby_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Ruby to use. Defaults to “2.0.0”.</p></li>
<li><p><strong>rubygems_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of RubyGems to use. Defaults to “2.2.2”.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RdsDbInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">RdsDbInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rds_db_instance_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks RDS DB Instance resource.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">my_instance</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">RdsDbInstance</span><span class="p">(</span><span class="s2">&quot;myInstance&quot;</span><span class="p">,</span>
    <span class="n">db_password</span><span class="o">=</span><span class="s2">&quot;somePass&quot;</span><span class="p">,</span>
    <span class="n">db_user</span><span class="o">=</span><span class="s2">&quot;someUser&quot;</span><span class="p">,</span>
    <span class="n">rds_db_instance_arn</span><span class="o">=</span><span class="n">aws_db_instance</span><span class="p">[</span><span class="s2">&quot;my_instance&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;my_stack&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db password</p></li>
<li><p><strong>db_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db username</p></li>
<li><p><strong>rds_db_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db instance to register for this stack. Changing this will force a new resource.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to register a db instance for. Changing this will force a new resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_password">
<code class="sig-name descname">db_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_password" title="Permalink to this definition">¶</a></dt>
<dd><p>A db password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_user">
<code class="sig-name descname">db_user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_user" title="Permalink to this definition">¶</a></dt>
<dd><p>A db username</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn">
<code class="sig-name descname">rds_db_instance_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The db instance to register for this stack. Changing this will force a new resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to register a db instance for. Changing this will force a new resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rds_db_instance_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RdsDbInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db password</p></li>
<li><p><strong>db_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db username</p></li>
<li><p><strong>rds_db_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db instance to register for this stack. Changing this will force a new resource.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to register a db instance for. Changing this will force a new resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Stack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">Stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">berkshelf_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_manager_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_manager_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_cookbooks_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_os</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssh_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_berkshelf</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_custom_cookbooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_opsworks_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks stack resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">main</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">Stack</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">custom_json</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2"> &quot;foobar&quot;: {</span>
<span class="s2">    &quot;version&quot;: &quot;1.0.0&quot;</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">default_instance_profile_arn</span><span class="o">=</span><span class="n">aws_iam_instance_profile</span><span class="p">[</span><span class="s2">&quot;opsworks&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west-1&quot;</span><span class="p">,</span>
    <span class="n">service_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;opsworks&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;foobar-stack&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p></li>
<li><p><strong>berkshelf_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Color to paint next to the stack’s resources in the OpsWorks console.</p></li>
<li><p><strong>configuration_manager_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration manager to use. Defaults to “Chef”.</p></li>
<li><p><strong>configuration_manager_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the configuration manager to use. Defaults to “11.4”.</p></li>
<li><p><strong>custom_cookbooks_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the entire stack.</p></li>
<li><p><strong>default_availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p></li>
<li><p><strong>default_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Instance Profile that created instances
will have by default.</p></li>
<li><p><strong>default_os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of OS that will be installed on instances by default.</p></li>
<li><p><strong>default_root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.</p></li>
<li><p><strong>default_ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>default_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p></li>
<li><p><strong>hostname_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p></li>
<li><p><strong>manage_berkshelf</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stack.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the region where the stack will exist.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that the OpsWorks service will act as.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_custom_cookbooks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the custom cookbook settings are
enabled.</p></li>
<li><p><strong>use_opsworks_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that this stack belongs to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_cookbooks_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SSH key to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the cookbooks resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.agent_version">
<code class="sig-name descname">agent_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.berkshelf_version">
<code class="sig-name descname">berkshelf_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.berkshelf_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.color">
<code class="sig-name descname">color</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.color" title="Permalink to this definition">¶</a></dt>
<dd><p>Color to paint next to the stack’s resources in the OpsWorks console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_name">
<code class="sig-name descname">configuration_manager_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration manager to use. Defaults to “Chef”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_version">
<code class="sig-name descname">configuration_manager_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the configuration manager to use. Defaults to “11.4”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_cookbooks_sources">
<code class="sig-name descname">custom_cookbooks_sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_cookbooks_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Password to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SSH key to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL where the cookbooks resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_json">
<code class="sig-name descname">custom_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the entire stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_availability_zone">
<code class="sig-name descname">default_availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_instance_profile_arn">
<code class="sig-name descname">default_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM Instance Profile that created instances
will have by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_os">
<code class="sig-name descname">default_os</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of OS that will be installed on instances by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_root_device_type">
<code class="sig-name descname">default_root_device_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_ssh_key_name">
<code class="sig-name descname">default_ssh_key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.default_subnet_id">
<code class="sig-name descname">default_subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.hostname_theme">
<code class="sig-name descname">hostname_theme</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.hostname_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.manage_berkshelf">
<code class="sig-name descname">manage_berkshelf</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.manage_berkshelf" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the region where the stack will exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that the OpsWorks service will act as.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.use_custom_cookbooks">
<code class="sig-name descname">use_custom_cookbooks</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_custom_cookbooks" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the custom cookbook settings are
enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.use_opsworks_security_groups">
<code class="sig-name descname">use_opsworks_security_groups</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_opsworks_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.Stack.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that this stack belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Stack.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">berkshelf_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_manager_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_manager_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_cookbooks_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_os</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssh_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_berkshelf</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_custom_cookbooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_opsworks_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Stack resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">&quot;LATEST&quot;</span></code>, OpsWorks will automatically install the latest version.</p></li>
<li><p><strong>berkshelf_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">manage_berkshelf</span></code> is enabled, the version of Berkshelf to use.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Color to paint next to the stack’s resources in the OpsWorks console.</p></li>
<li><p><strong>configuration_manager_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration manager to use. Defaults to “Chef”.</p></li>
<li><p><strong>configuration_manager_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the configuration manager to use. Defaults to “11.4”.</p></li>
<li><p><strong>custom_cookbooks_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">use_custom_cookbooks</span></code> is set, provide this sub-object as
described below.</p></li>
<li><p><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the entire stack.</p></li>
<li><p><strong>default_availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default. This is required unless you set <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>.</p></li>
<li><p><strong>default_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Instance Profile that created instances
will have by default.</p></li>
<li><p><strong>default_os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of OS that will be installed on instances by default.</p></li>
<li><p><strong>default_root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.</p></li>
<li><p><strong>default_ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</p></li>
<li><p><strong>default_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the subnet in which instances will be created by default. Mandatory
if <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> is set, and forbidden if it isn’t.</p></li>
<li><p><strong>hostname_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p></li>
<li><p><strong>manage_berkshelf</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stack.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the region where the stack will exist.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that the OpsWorks service will act as.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_custom_cookbooks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the custom cookbook settings are
enabled.</p></li>
<li><p><strong>use_opsworks_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that this stack belongs to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_cookbooks_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For sources that are version-aware, the revision to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SSH key to use when authenticating to the source. The provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of source to use. For example, “archive”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL where the cookbooks resource can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Username to use when authenticating to the source.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.Stack.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.Stack.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.StaticWebLayer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">StaticWebLayer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks static web server layer resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">web</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">StaticWebLayer</span><span class="p">(</span><span class="s2">&quot;web&quot;</span><span class="p">,</span> <span class="n">stack_id</span><span class="o">=</span><span class="n">aws_opsworks_stack</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips">
<code class="sig-name descname">auto_assign_elastic_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips">
<code class="sig-name descname">auto_assign_public_ips</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn">
<code class="sig-name descname">custom_instance_profile_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids">
<code class="sig-name descname">custom_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown">
<code class="sig-name descname">drain_elb_on_shutdown</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.ebs_volumes">
<code class="sig-name descname">ebs_volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer">
<code class="sig-name descname">elastic_load_balancer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot">
<code class="sig-name descname">install_updates_on_boot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout">
<code class="sig-name descname">instance_shutdown_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.stack_id">
<code class="sig-name descname">stack_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.system_packages">
<code class="sig-name descname">system_packages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances">
<code class="sig-name descname">use_ebs_optimized_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_assign_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_configure_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_deploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_instance_profile_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_setup_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_shutdown_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_undeploy_recipes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drain_elb_on_shutdown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_updates_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_shutdown_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ebs_optimized_instances</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StaticWebLayer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name(ARN) of the layer.</p></li>
<li><p><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</p></li>
<li><p><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</p></li>
<li><p><strong>custom_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM profile that will be used for the layer’s instances.</p></li>
<li><p><strong>custom_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids for a set of security groups to apply to the layer’s instances.</p></li>
<li><p><strong>drain_elb_on_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Elastic Load Balancing connection draining.</p></li>
<li><p><strong>ebs_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ebs_volume</span></code> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p></li>
<li><p><strong>elastic_load_balancer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an Elastic Load Balancer to attach to this layer</p></li>
<li><p><strong>install_updates_on_boot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to install OS and package updates on each instance when it boots.</p></li>
<li><p><strong>instance_shutdown_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the layer.</p></li>
<li><p><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the layer will belong to.</p></li>
<li><p><strong>system_packages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of a set of system packages to install on the layer’s instances.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>use_ebs_optimized_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EBS-optimized instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For PIOPS volumes, the IOPS per disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the EBS volume on the layer’s instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of disks to use for the EBS volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">raidLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RAID level to use for the volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of volume to create. This may be <code class="docutils literal notranslate"><span class="pre">standard</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">io1</span></code> or <code class="docutils literal notranslate"><span class="pre">gp2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.UserProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.opsworks.</code><code class="sig-name descname">UserProfile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_self_management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks User Profile resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">my_profile</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">opsworks</span><span class="o">.</span><span class="n">UserProfile</span><span class="p">(</span><span class="s2">&quot;myProfile&quot;</span><span class="p">,</span>
    <span class="n">ssh_username</span><span class="o">=</span><span class="s2">&quot;my_user&quot;</span><span class="p">,</span>
    <span class="n">user_arn</span><span class="o">=</span><span class="n">aws_iam_user</span><span class="p">[</span><span class="s2">&quot;user&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_self_management</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users can specify their own SSH public key through the My Settings page</p></li>
<li><p><strong>ssh_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users public key</p></li>
<li><p><strong>ssh_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ssh username, with witch this user wants to log in</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.opsworks.UserProfile.allow_self_management">
<code class="sig-name descname">allow_self_management</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.allow_self_management" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether users can specify their own SSH public key through the My Settings page</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_public_key">
<code class="sig-name descname">ssh_public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The users public key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_username">
<code class="sig-name descname">ssh_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The ssh username, with witch this user wants to log in</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.opsworks.UserProfile.user_arn">
<code class="sig-name descname">user_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.UserProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_self_management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_self_management</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users can specify their own SSH public key through the My Settings page</p></li>
<li><p><strong>ssh_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users public key</p></li>
<li><p><strong>ssh_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ssh username, with witch this user wants to log in</p></li>
<li><p><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.opsworks.UserProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.opsworks.UserProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
