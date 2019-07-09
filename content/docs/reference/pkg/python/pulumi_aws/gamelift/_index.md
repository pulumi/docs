---
---

<div class="section" id="module-pulumi_aws.gamelift">
<span id="gamelift"></span><h1>gamelift<a class="headerlink" href="#module-pulumi_aws.gamelift" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.gamelift.Alias">
<em class="property">class </em><code class="descclassname">pulumi_aws.gamelift.</code><code class="descname">Alias</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>routing_strategy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Gamelift Alias resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the alias.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the alias.</li>
<li><strong>routing_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the fleet and/or routing type to use for the alias.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_alias.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Alias.routing_strategy">
<code class="descname">routing_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Alias.routing_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the fleet and/or routing type to use for the alias.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Alias.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Alias.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Build">
<em class="property">class </em><code class="descclassname">pulumi_aws.gamelift.</code><code class="descname">Build</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>operating_system=None</em>, <em>storage_location=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Gamelift Build resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the build</li>
<li><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system that the game server binaries are built to run on. e.g. <code class="docutils literal notranslate"><span class="pre">WINDOWS_2012</span></code> or <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>.</li>
<li><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information indicating where your game build files are stored. See below.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version that is associated with this build.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_build.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the build</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.operating_system">
<code class="descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system that the game server binaries are built to run on. e.g. <code class="docutils literal notranslate"><span class="pre">WINDOWS_2012</span></code> or <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.storage_location">
<code class="descname">storage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.storage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Information indicating where your game build files are stored. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Build.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Build.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version that is associated with this build.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Build.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Build.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Build.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Fleet">
<em class="property">class </em><code class="descclassname">pulumi_aws.gamelift.</code><code class="descname">Fleet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>build_id=None</em>, <em>description=None</em>, <em>ec2_inbound_permissions=None</em>, <em>ec2_instance_type=None</em>, <em>metric_groups=None</em>, <em>name=None</em>, <em>new_game_session_protection_policy=None</em>, <em>resource_creation_limit_policy=None</em>, <em>runtime_configuration=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Gamelift Fleet resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>build_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Gamelift Build to be deployed on the fleet.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the fleet.</li>
<li><strong>ec2_inbound_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.</li>
<li><strong>ec2_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an EC2 instance type. e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code></li>
<li><strong>metric_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the fleet.</li>
<li><strong>new_game_session_protection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Game session protection policy to apply to all instances in this fleet. e.g. <code class="docutils literal notranslate"><span class="pre">FullProtection</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NoProtection</span></code>.</li>
<li><strong>resource_creation_limit_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.</li>
<li><strong>runtime_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Instructions for launching server processes on each instance in the fleet. See below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_fleet.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fleet ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.build_id">
<code class="descname">build_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.build_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Gamelift Build to be deployed on the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.ec2_inbound_permissions">
<code class="descname">ec2_inbound_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.ec2_inbound_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.ec2_instance_type">
<code class="descname">ec2_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.ec2_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an EC2 instance type. e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.metric_groups">
<code class="descname">metric_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.metric_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.new_game_session_protection_policy">
<code class="descname">new_game_session_protection_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.new_game_session_protection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Game session protection policy to apply to all instances in this fleet. e.g. <code class="docutils literal notranslate"><span class="pre">FullProtection</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NoProtection</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.operating_system">
<code class="descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system of the fleet’s computing resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.resource_creation_limit_policy">
<code class="descname">resource_creation_limit_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.resource_creation_limit_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.Fleet.runtime_configuration">
<code class="descname">runtime_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.runtime_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Instructions for launching server processes on each instance in the fleet. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.Fleet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.Fleet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.Fleet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.GameSessionQueue">
<em class="property">class </em><code class="descclassname">pulumi_aws.gamelift.</code><code class="descname">GameSessionQueue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destinations=None</em>, <em>name=None</em>, <em>player_latency_policies=None</em>, <em>timeout_in_seconds=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Gamelift Game Session Queue resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of fleet/alias ARNs used by session queue for placing game sessions.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the session queue.</li>
<li><strong>player_latency_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more policies used to choose fleet based on player latency. See below.</li>
<li><strong>timeout_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum time a game session request can remain in the queue.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/gamelift_game_session_queue.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Game Session Queue ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.destinations">
<code class="descname">destinations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.destinations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of fleet/alias ARNs used by session queue for placing game sessions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the session queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.player_latency_policies">
<code class="descname">player_latency_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.player_latency_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more policies used to choose fleet based on player latency. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.gamelift.GameSessionQueue.timeout_in_seconds">
<code class="descname">timeout_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.timeout_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum time a game session request can remain in the queue.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.gamelift.GameSessionQueue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.gamelift.GameSessionQueue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.gamelift.GameSessionQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
