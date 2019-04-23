<div class="section" id="module-pulumi_aws.licensemanager">
<span id="licensemanager"></span><h1>licensemanager<a class="headerlink" href="#module-pulumi_aws.licensemanager" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.licensemanager.Association">
<em class="property">class </em><code class="descclassname">pulumi_aws.licensemanager.</code><code class="descname">Association</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>license_configuration_arn=None</em>, <em>resource_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a License Manager association.</p>
<blockquote>
<div><strong>Note:</strong> License configurations can also be associated with launch templates by specifying the <code class="docutils literal notranslate"><span class="pre">license_specifications</span></code> block for an <code class="docutils literal notranslate"><span class="pre">aws_launch_template</span></code>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>license_configuration_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the license configuration.</li>
<li><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource associated with the license configuration.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.licensemanager.Association.license_configuration_arn">
<code class="descname">license_configuration_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.Association.license_configuration_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the license configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.Association.resource_arn">
<code class="descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.Association.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the resource associated with the license configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.licensemanager.Association.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.Association.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.LicenseConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.licensemanager.</code><code class="descname">LicenseConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>license_count=None</em>, <em>license_count_hard_limit=None</em>, <em>license_counting_type=None</em>, <em>license_rules=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a License Manager license configuration resource.</p>
<blockquote>
<div><strong>Note:</strong> Removing the <code class="docutils literal notranslate"><span class="pre">license_count</span></code> attribute is not supported by the License Manager API - use <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">taint</span> <span class="pre">aws_licensemanager_license_configuration.&lt;id&gt;</span></code> to recreate the resource instead.</div></blockquote>
<p>License rules should be in the format of <code class="docutils literal notranslate"><span class="pre">#RuleType=RuleValue</span></code>. Supported rule types:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">minimumVcpus</span></code> - Resource must have minimum vCPU count in order to use the license. Default: 1</li>
<li><code class="docutils literal notranslate"><span class="pre">maximumVcpus</span></code> - Resource must have maximum vCPU count in order to use the license. Default: unbounded, limit: 10000</li>
<li><code class="docutils literal notranslate"><span class="pre">minimumCores</span></code> - Resource must have minimum core count in order to use the license. Default: 1</li>
<li><code class="docutils literal notranslate"><span class="pre">maximumCores</span></code> - Resource must have maximum core count in order to use the license. Default: unbounded, limit: 10000</li>
<li><code class="docutils literal notranslate"><span class="pre">minimumSockets</span></code> - Resource must have minimum socket count in order to use the license. Default: 1</li>
<li><code class="docutils literal notranslate"><span class="pre">maximumSockets</span></code> - Resource must have maximum socket count in order to use the license. Default: unbounded, limit: 10000</li>
<li><code class="docutils literal notranslate"><span class="pre">allowedTenancy</span></code> - Defines where the license can be used. If set, restricts license usage to selected tenancies. Specify a comma delimited list of <code class="docutils literal notranslate"><span class="pre">EC2-Default</span></code>, <code class="docutils literal notranslate"><span class="pre">EC2-DedicatedHost</span></code>, <code class="docutils literal notranslate"><span class="pre">EC2-DedicatedInstance</span></code></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the license configuration.</li>
<li><strong>license_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of licenses managed by the license configuration.</li>
<li><strong>license_count_hard_limit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets the number of available licenses as a hard limit.</li>
<li><strong>license_counting_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dimension to use to track license inventory. Specify either <code class="docutils literal notranslate"><span class="pre">vCPU</span></code>, <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Core</span></code> or <code class="docutils literal notranslate"><span class="pre">Socket</span></code>.</li>
<li><strong>license_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of configured License Manager rules.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the license configuration.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the license configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_count">
<code class="descname">license_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of licenses managed by the license configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_count_hard_limit">
<code class="descname">license_count_hard_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_count_hard_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the number of available licenses as a hard limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_counting_type">
<code class="descname">license_counting_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_counting_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Dimension to use to track license inventory. Specify either <code class="docutils literal notranslate"><span class="pre">vCPU</span></code>, <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Core</span></code> or <code class="docutils literal notranslate"><span class="pre">Socket</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_rules">
<code class="descname">license_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of configured License Manager rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the license configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
