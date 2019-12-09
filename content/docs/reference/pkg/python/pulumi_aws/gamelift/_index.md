---
title: Module gamelift
title_tag: Module gamelift | Package pulumi_aws | Python SDK
linktitle: gamelift
notitle: true
---

<div class="section" id="gamelift">
<h1>gamelift<a class="headerlink" href="#gamelift" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.gamelift"></span><dl class="class">
<dt id="pulumi_aws.gamelift.Alias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.gamelift.</code><code class="sig-name descname">Alias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">routing_strategy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Gamelift Alias resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the alias.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the alias.</p></li>
<li><p><strong>routing_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the fleet and/or routing type to use for the alias.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routing_strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Gamelift Fleet to point the alias to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Message text to be used with the <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code> routing strategy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of routing strategy. e.g. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code> or <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.routing_strategy">
<code class="sig-name descname">routing_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.routing_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the fleet and/or routing type to use for the alias.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the Gamelift Fleet to point the alias to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Message text to be used with the <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code> routing strategy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of routing strategy. e.g. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code> or <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Alias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">routing_strategy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias ARN.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the alias.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the alias.</p></li>
<li><p><strong>routing_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the fleet and/or routing type to use for the alias.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routing_strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Gamelift Fleet to point the alias to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Message text to be used with the <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code> routing strategy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of routing strategy. e.g. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code> or <code class="docutils literal notranslate"><span class="pre">TERMINAL</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Alias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Alias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.gamelift.Build">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.gamelift.</code><code class="sig-name descname">Build</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operating_system=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Gamelift Build resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the build</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system that the game server binaries are built to run on. e.g. <code class="docutils literal notranslate"><span class="pre">WINDOWS_2012</span></code> or <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information indicating where your game build files are stored. See below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version that is associated with this build.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of your S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the zip file containing your build files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the access role that allows Amazon GameLift to access your S3 bucket.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the build</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.operating_system">
<code class="sig-name descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system that the game server binaries are built to run on. e.g. <code class="docutils literal notranslate"><span class="pre">WINDOWS_2012</span></code> or <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.storage_location">
<code class="sig-name descname">storage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.storage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Information indicating where your game build files are stored. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of your S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the zip file containing your build files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the access role that allows Amazon GameLift to access your S3 bucket.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version that is associated with this build.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Build.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operating_system=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Build resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the build</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system that the game server binaries are built to run on. e.g. <code class="docutils literal notranslate"><span class="pre">WINDOWS_2012</span></code> or <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information indicating where your game build files are stored. See below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version that is associated with this build.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of your S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the zip file containing your build files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the access role that allows Amazon GameLift to access your S3 bucket.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Build.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Build.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.gamelift.Fleet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.gamelift.</code><code class="sig-name descname">Fleet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">build_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ec2_inbound_permissions=None</em>, <em class="sig-param">ec2_instance_type=None</em>, <em class="sig-param">metric_groups=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">new_game_session_protection_policy=None</em>, <em class="sig-param">resource_creation_limit_policy=None</em>, <em class="sig-param">runtime_configuration=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Gamelift Fleet resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>build_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Gamelift Build to be deployed on the fleet.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the fleet.</p></li>
<li><p><strong>ec2_inbound_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.</p></li>
<li><p><strong>ec2_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an EC2 instance type. e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code></p></li>
<li><p><strong>metric_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the fleet.</p></li>
<li><p><strong>new_game_session_protection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Game session protection policy to apply to all instances in this fleet. e.g. <code class="docutils literal notranslate"><span class="pre">FullProtection</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NoProtection</span></code>.</p></li>
<li><p><strong>resource_creation_limit_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.</p></li>
<li><p><strong>runtime_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Instructions for launching server processes on each instance in the fleet. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ec2_inbound_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Starting value for a range of allowed port numbers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Range of allowed IP addresses expressed in CIDR notation. e.g. <code class="docutils literal notranslate"><span class="pre">000.000.000.000/[subnet</span> <span class="pre">mask]</span></code> or <code class="docutils literal notranslate"><span class="pre">0.0.0.0/[subnet</span> <span class="pre">mask]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network communication protocol used by the fleet. e.g. <code class="docutils literal notranslate"><span class="pre">TCP</span></code> or <code class="docutils literal notranslate"><span class="pre">UDP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than <code class="docutils literal notranslate"><span class="pre">from_port</span></code>.</p></li>
</ul>
<p>The <strong>resource_creation_limit_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">newGameSessionsPerCreator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of game sessions that an individual can create during the policy period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyPeriodInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Time span used in evaluating the resource creation limit policy.</p></li>
</ul>
<p>The <strong>runtime_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gameSessionActivationTimeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum amount of time (in seconds) that a game session can remain in status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentGameSessionActivations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of game sessions with status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code> to allow on an instance simultaneously.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">concurrentExecutions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of server processes using this configuration to run concurrently on an instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances <code class="docutils literal notranslate"><span class="pre">C:\game</span></code>, and for Linux instances <code class="docutils literal notranslate"><span class="pre">/local/game</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Optional list of parameters to pass to the server executable on launch.</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fleet ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.build_id">
<code class="sig-name descname">build_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.build_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Gamelift Build to be deployed on the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.ec2_inbound_permissions">
<code class="sig-name descname">ec2_inbound_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.ec2_inbound_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Starting value for a range of allowed port numbers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Range of allowed IP addresses expressed in CIDR notation. e.g. <code class="docutils literal notranslate"><span class="pre">000.000.000.000/[subnet</span> <span class="pre">mask]</span></code> or <code class="docutils literal notranslate"><span class="pre">0.0.0.0/[subnet</span> <span class="pre">mask]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Network communication protocol used by the fleet. e.g. <code class="docutils literal notranslate"><span class="pre">TCP</span></code> or <code class="docutils literal notranslate"><span class="pre">UDP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than <code class="docutils literal notranslate"><span class="pre">from_port</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.ec2_instance_type">
<code class="sig-name descname">ec2_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.ec2_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an EC2 instance type. e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.metric_groups">
<code class="sig-name descname">metric_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.metric_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.new_game_session_protection_policy">
<code class="sig-name descname">new_game_session_protection_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.new_game_session_protection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Game session protection policy to apply to all instances in this fleet. e.g. <code class="docutils literal notranslate"><span class="pre">FullProtection</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NoProtection</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.operating_system">
<code class="sig-name descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system of the fleet’s computing resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.resource_creation_limit_policy">
<code class="sig-name descname">resource_creation_limit_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.resource_creation_limit_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">newGameSessionsPerCreator</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of game sessions that an individual can create during the policy period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyPeriodInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Time span used in evaluating the resource creation limit policy.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.runtime_configuration">
<code class="sig-name descname">runtime_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.runtime_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Instructions for launching server processes on each instance in the fleet. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gameSessionActivationTimeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum amount of time (in seconds) that a game session can remain in status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentGameSessionActivations</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of game sessions with status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code> to allow on an instance simultaneously.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">concurrentExecutions</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of server processes using this configuration to run concurrently on an instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances <code class="docutils literal notranslate"><span class="pre">C:\game</span></code>, and for Linux instances <code class="docutils literal notranslate"><span class="pre">/local/game</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Optional list of parameters to pass to the server executable on launch.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Fleet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">build_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ec2_inbound_permissions=None</em>, <em class="sig-param">ec2_instance_type=None</em>, <em class="sig-param">log_paths=None</em>, <em class="sig-param">metric_groups=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">new_game_session_protection_policy=None</em>, <em class="sig-param">operating_system=None</em>, <em class="sig-param">resource_creation_limit_policy=None</em>, <em class="sig-param">runtime_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Fleet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fleet ARN.</p></li>
<li><p><strong>build_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Gamelift Build to be deployed on the fleet.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the fleet.</p></li>
<li><p><strong>ec2_inbound_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.</p></li>
<li><p><strong>ec2_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an EC2 instance type. e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code></p></li>
<li><p><strong>metric_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the fleet.</p></li>
<li><p><strong>new_game_session_protection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Game session protection policy to apply to all instances in this fleet. e.g. <code class="docutils literal notranslate"><span class="pre">FullProtection</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NoProtection</span></code>.</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system of the fleet’s computing resources.</p></li>
<li><p><strong>resource_creation_limit_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.</p></li>
<li><p><strong>runtime_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Instructions for launching server processes on each instance in the fleet. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ec2_inbound_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Starting value for a range of allowed port numbers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Range of allowed IP addresses expressed in CIDR notation. e.g. <code class="docutils literal notranslate"><span class="pre">000.000.000.000/[subnet</span> <span class="pre">mask]</span></code> or <code class="docutils literal notranslate"><span class="pre">0.0.0.0/[subnet</span> <span class="pre">mask]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network communication protocol used by the fleet. e.g. <code class="docutils literal notranslate"><span class="pre">TCP</span></code> or <code class="docutils literal notranslate"><span class="pre">UDP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than <code class="docutils literal notranslate"><span class="pre">from_port</span></code>.</p></li>
</ul>
<p>The <strong>resource_creation_limit_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">newGameSessionsPerCreator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of game sessions that an individual can create during the policy period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyPeriodInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Time span used in evaluating the resource creation limit policy.</p></li>
</ul>
<p>The <strong>runtime_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gameSessionActivationTimeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum amount of time (in seconds) that a game session can remain in status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentGameSessionActivations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of game sessions with status <code class="docutils literal notranslate"><span class="pre">ACTIVATING</span></code> to allow on an instance simultaneously.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">concurrentExecutions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of server processes using this configuration to run concurrently on an instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances <code class="docutils literal notranslate"><span class="pre">C:\game</span></code>, and for Linux instances <code class="docutils literal notranslate"><span class="pre">/local/game</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Optional list of parameters to pass to the server executable on launch.</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Fleet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Fleet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.gamelift.GameSessionQueue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.gamelift.</code><code class="sig-name descname">GameSessionQueue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destinations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">player_latency_policies=None</em>, <em class="sig-param">timeout_in_seconds=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Gamelift Game Session Queue resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of fleet/alias ARNs used by session queue for placing game sessions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the session queue.</p></li>
<li><p><strong>player_latency_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more policies used to choose fleet based on player latency. See below.</p></li>
<li><p><strong>timeout_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum time a game session request can remain in the queue.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>player_latency_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maximumIndividualPlayerLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum latency value that is allowed for any player.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Length of time that the policy is enforced while placing a new game session. Absence of value for this attribute means that the policy is enforced until the queue times out.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Game Session Queue ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.destinations">
<code class="sig-name descname">destinations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.destinations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of fleet/alias ARNs used by session queue for placing game sessions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the session queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.player_latency_policies">
<code class="sig-name descname">player_latency_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.player_latency_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more policies used to choose fleet based on player latency. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maximumIndividualPlayerLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum latency value that is allowed for any player.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Length of time that the policy is enforced while placing a new game session. Absence of value for this attribute means that the policy is enforced until the queue times out.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.timeout_in_seconds">
<code class="sig-name descname">timeout_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.timeout_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum time a game session request can remain in the queue.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.GameSessionQueue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">destinations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">player_latency_policies=None</em>, <em class="sig-param">timeout_in_seconds=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GameSessionQueue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Game Session Queue ARN.</p></li>
<li><p><strong>destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of fleet/alias ARNs used by session queue for placing game sessions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the session queue.</p></li>
<li><p><strong>player_latency_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more policies used to choose fleet based on player latency. See below.</p></li>
<li><p><strong>timeout_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum time a game session request can remain in the queue.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>player_latency_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maximumIndividualPlayerLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum latency value that is allowed for any player.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Length of time that the policy is enforced while placing a new game session. Absence of value for this attribute means that the policy is enforced until the queue times out.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.GameSessionQueue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.GameSessionQueue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
