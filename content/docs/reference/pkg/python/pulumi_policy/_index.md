---
title: Package pulumi_policy
title_tag: Package pulumi_policy | Python SDK
linktitle: pulumi_policy
notitle: true
---

{{< resource-docs-alert "policy" >}}

<section id="module-pulumi_policy">
<span id="pulumi-policy"></span><h1>Pulumi Policy<a class="headerlink" href="#module-pulumi_policy" title="Permalink to this heading"></a></h1>
<p>The Pulumi Policy SDK for Python.</p>
<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.EnforcementLevel">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">EnforcementLevel</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.EnforcementLevel" title="Permalink to this definition"></a></dt>
<dd><p>Indicates the impact of a policy violation.</p>
</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.Policy">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">Policy</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">enforcement_level</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">config_schema</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.policy.PolicyConfigSchema"><span class="pre">PolicyConfigSchema</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.Policy" title="Permalink to this definition"></a></dt>
<dd><p>A policy function that returns true if a resource definition violates some policy (e.g., “no
public S3 buckets”), and a set of metadata useful for generating helpful messages when the policy
is violated.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
<li><p><strong>config_schema</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.PolicyConfigSchema"><em>PolicyConfigSchema</em></a><em>]</em>) – This policy’s configuration schema.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.Policy.name">
<span class="sig-name descname"><span class="pre">name</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.Policy.name" title="Permalink to this definition"></a></dt>
<dd><p>An ID for the policy. Must be unique within the current policy set.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.Policy.description">
<span class="sig-name descname"><span class="pre">description</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.Policy.description" title="Permalink to this definition"></a></dt>
<dd><p>A brief description of the policy rule. e.g., “S3 buckets should have default encryption
enabled.”</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.Policy.enforcement_level">
<span class="sig-name descname"><span class="pre">enforcement_level</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.Policy.enforcement_level" title="Permalink to this definition"></a></dt>
<dd><p>Indicates what to do on policy violation, e.g., block deployment but allow override with
proper permissions.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.Policy.config_schema">
<span class="sig-name descname"><span class="pre">config_schema</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.policy.PolicyConfigSchema"><span class="pre">PolicyConfigSchema</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.Policy.config_schema" title="Permalink to this definition"></a></dt>
<dd><p>This policy’s configuration schema.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyConfigSchema">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyConfigSchema</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">properties</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">required</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyConfigSchema" title="Permalink to this definition"></a></dt>
<dd><p>Represents the configuration schema for a policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>properties</strong> (<em>Dict</em><em>[</em><em>str</em><em>, </em><em>Dict</em><em>[</em><em>str</em><em>, </em><em>Any</em><em>]</em><em>]</em>) – The policy’s configuration properties.</p></li>
<li><p><strong>required</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The configuration properties that are required.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyConfigSchema.properties">
<span class="sig-name descname"><span class="pre">properties</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyConfigSchema.properties" title="Permalink to this definition"></a></dt>
<dd><p>The policy’s configuration properties.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyConfigSchema.required">
<span class="sig-name descname"><span class="pre">required</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.PolicyConfigSchema.required" title="Permalink to this definition"></a></dt>
<dd><p>The configuration properties that are required.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyCustomTimeouts">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyCustomTimeouts</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">create_seconds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">update_seconds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">delete_seconds</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts" title="Permalink to this definition"></a></dt>
<dd><p>Custom timeout options.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyCustomTimeouts.create_seconds">
<span class="sig-name descname"><span class="pre">create_seconds</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span></em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.create_seconds" title="Permalink to this definition"></a></dt>
<dd><p>The create resource timeout.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyCustomTimeouts.update_seconds">
<span class="sig-name descname"><span class="pre">update_seconds</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span></em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.update_seconds" title="Permalink to this definition"></a></dt>
<dd><p>The update resource timeout.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyCustomTimeouts.delete_seconds">
<span class="sig-name descname"><span class="pre">delete_seconds</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span></em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.delete_seconds" title="Permalink to this definition"></a></dt>
<dd><p>The delete resource timeout.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyPack">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyPack</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">policies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.Policy" title="pulumi_policy.policy.Policy"><span class="pre">Policy</span></a><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">enforcement_level</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">initial_config</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyPack" title="Permalink to this definition"></a></dt>
<dd><p>A policy pack contains one or more policies to enforce.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the policy pack.</p></li>
<li><p><strong>policies</strong> (<em>List</em><em>[</em><a class="reference internal" href="#pulumi_policy.Policy" title="pulumi_policy.Policy"><em>Policy</em></a><em>]</em>) – The policies associated with a policy pack.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy
violation, e.g., block deployment but allow override with
proper permissions. This is the default used for all policies in the policy pack.
Individual policies can override.</p></li>
<li><p><strong>initial_config</strong> (<em>Optional</em><em>[</em><em>Dict</em><em>[</em><em>str</em><em>, </em><em>Union</em><em>[</em><em>'EnforcementLevel'</em><em>, </em><em>Dict</em><em>[</em><em>str</em><em>, </em><em>Any</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Initial
configuration for the policy pack. Allows specifying configuration programmatically from reusable
policy libraries.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyProviderResource">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyProviderResource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">resource_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">props</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">urn</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyProviderResource" title="Permalink to this definition"></a></dt>
<dd><p>Information about the provider.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyProviderResource.resource_type">
<span class="sig-name descname"><span class="pre">resource_type</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.resource_type" title="Permalink to this definition"></a></dt>
<dd><p>The type of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyProviderResource.props">
<span class="sig-name descname"><span class="pre">props</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.props" title="Permalink to this definition"></a></dt>
<dd><p>The properties of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyProviderResource.urn">
<span class="sig-name descname"><span class="pre">urn</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.urn" title="Permalink to this definition"></a></dt>
<dd><p>The URN of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyProviderResource.name">
<span class="sig-name descname"><span class="pre">name</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the provider resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyResource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">resource_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">props</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">urn</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">opts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyResourceOptions" title="pulumi_policy.policy.PolicyResourceOptions"><span class="pre">PolicyResourceOptions</span></a></span></em>, <em class="sig-param"><span class="n"><span class="pre">provider</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyProviderResource" title="pulumi_policy.policy.PolicyProviderResource"><span class="pre">PolicyProviderResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">parent</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">dependencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">property_dependencies</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyResource" title="Permalink to this definition"></a></dt>
<dd><p>PolicyResource represents a resource in the stack.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.resource_type">
<span class="sig-name descname"><span class="pre">resource_type</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.resource_type" title="Permalink to this definition"></a></dt>
<dd><p>The type of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.props">
<span class="sig-name descname"><span class="pre">props</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.props" title="Permalink to this definition"></a></dt>
<dd><p>The outputs of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.urn">
<span class="sig-name descname"><span class="pre">urn</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.urn" title="Permalink to this definition"></a></dt>
<dd><p>The URN of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.name">
<span class="sig-name descname"><span class="pre">name</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.opts">
<span class="sig-name descname"><span class="pre">opts</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyResourceOptions" title="pulumi_policy.policy.PolicyResourceOptions"><span class="pre">PolicyResourceOptions</span></a></em><a class="headerlink" href="#pulumi_policy.PolicyResource.opts" title="Permalink to this definition"></a></dt>
<dd><p>The options of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.provider">
<span class="sig-name descname"><span class="pre">provider</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyProviderResource" title="pulumi_policy.policy.PolicyProviderResource"><span class="pre">PolicyProviderResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.parent">
<span class="sig-name descname"><span class="pre">parent</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.parent" title="Permalink to this definition"></a></dt>
<dd><p>An optional parent that this resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.dependencies">
<span class="sig-name descname"><span class="pre">dependencies</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.dependencies" title="Permalink to this definition"></a></dt>
<dd><p>The dependencies of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResource.property_dependencies">
<span class="sig-name descname"><span class="pre">property_dependencies</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Dict</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResource.property_dependencies" title="Permalink to this definition"></a></dt>
<dd><p>The set of dependencies that affect each property.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">PolicyResourceOptions</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">protect</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ignore_changes</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">delete_before_replace</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">aliases</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">custom_timeouts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyCustomTimeouts" title="pulumi_policy.policy.PolicyCustomTimeouts"><span class="pre">PolicyCustomTimeouts</span></a></span></em>, <em class="sig-param"><span class="n"><span class="pre">additional_secret_outputs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions" title="Permalink to this definition"></a></dt>
<dd><p>PolicyResourceOptions is the bag of settings that control a resource’s behavior.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.protect">
<span class="sig-name descname"><span class="pre">protect</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.protect" title="Permalink to this definition"></a></dt>
<dd><p>When set to true, protect ensures this resource cannot be deleted.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.ignore_changes">
<span class="sig-name descname"><span class="pre">ignore_changes</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.ignore_changes" title="Permalink to this definition"></a></dt>
<dd><p>Ignore changes to any of the specified properties.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.delete_before_replace">
<span class="sig-name descname"><span class="pre">delete_before_replace</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.delete_before_replace" title="Permalink to this definition"></a></dt>
<dd><p>When set to true, indicates that this resource should be deleted before
its replacement is created when replacement is necessary.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.aliases">
<span class="sig-name descname"><span class="pre">aliases</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.aliases" title="Permalink to this definition"></a></dt>
<dd><p>Additional URNs that should be aliased to this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.custom_timeouts">
<span class="sig-name descname"><span class="pre">custom_timeouts</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyCustomTimeouts" title="pulumi_policy.policy.PolicyCustomTimeouts"><span class="pre">PolicyCustomTimeouts</span></a></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.custom_timeouts" title="Permalink to this definition"></a></dt>
<dd><p>Custom timeouts for resource create, update, and delete operations.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.PolicyResourceOptions.additional_secret_outputs">
<span class="sig-name descname"><span class="pre">additional_secret_outputs</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.additional_secret_outputs" title="Permalink to this definition"></a></dt>
<dd><p>Outputs that should always be treated as secrets.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">ResourceValidationArgs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">resource_type</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">props</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">urn</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">opts</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyResourceOptions" title="pulumi_policy.policy.PolicyResourceOptions"><span class="pre">PolicyResourceOptions</span></a></span></em>, <em class="sig-param"><span class="n"><span class="pre">provider</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyProviderResource" title="pulumi_policy.policy.PolicyProviderResource"><span class="pre">PolicyProviderResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">config</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs" title="Permalink to this definition"></a></dt>
<dd><p>ResourceValidationArgs is the argument bag passed to a resource validation.</p>
<dl class="py method">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.get_config">
<span class="sig-name descname"><span class="pre">get_config</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.get_config" title="Permalink to this definition"></a></dt>
<dd><p>Returns configuration for the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.resource_type">
<span class="sig-name descname"><span class="pre">resource_type</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.resource_type" title="Permalink to this definition"></a></dt>
<dd><p>The type of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.props">
<span class="sig-name descname"><span class="pre">props</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.props" title="Permalink to this definition"></a></dt>
<dd><p>The inputs of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.urn">
<span class="sig-name descname"><span class="pre">urn</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.urn" title="Permalink to this definition"></a></dt>
<dd><p>The URN of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.name">
<span class="sig-name descname"><span class="pre">name</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.opts">
<span class="sig-name descname"><span class="pre">opts</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyResourceOptions" title="pulumi_policy.policy.PolicyResourceOptions"><span class="pre">PolicyResourceOptions</span></a></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.opts" title="Permalink to this definition"></a></dt>
<dd><p>The options of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationArgs.provider">
<span class="sig-name descname"><span class="pre">provider</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pulumi_policy.PolicyProviderResource" title="pulumi_policy.policy.PolicyProviderResource"><span class="pre">PolicyProviderResource</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider of the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.ResourceValidationPolicy">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">ResourceValidationPolicy</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">validate</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.ResourceValidationArgs" title="pulumi_policy.policy.ResourceValidationArgs"><span class="pre">ResourceValidationArgs</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Awaitable</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.ResourceValidationArgs" title="pulumi_policy.policy.ResourceValidationArgs"><span class="pre">ResourceValidationArgs</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Awaitable</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">enforcement_level</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">config_schema</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.policy.PolicyConfigSchema"><span class="pre">PolicyConfigSchema</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.ResourceValidationPolicy" title="Permalink to this definition"></a></dt>
<dd><p>ResourceValidationPolicy is a policy that validates a resource definition.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>validate</strong> (<em>Optional</em><em>[</em><em>Union</em><em>[</em><em>ResourceValidation</em><em>, </em><em>List</em><em>[</em><em>ResourceValidation</em><em>]</em><em>]</em><em>]</em>) – A callback function
that validates if a resource definition violates a policy (e.g. “S3 buckets can’t be public”).
A single callback function can be specified, or multiple functions, which are called in order.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
<li><p><strong>config_schema</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.PolicyConfigSchema"><em>PolicyConfigSchema</em></a><em>]</em>) – This policy’s configuration schema.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.StackValidationArgs">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">StackValidationArgs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">resources</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">config</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.StackValidationArgs" title="Permalink to this definition"></a></dt>
<dd><p>StackValidationArgs is the argument bag passed to a stack validation.</p>
<dl class="py method">
<dt class="sig sig-object py" id="pulumi_policy.StackValidationArgs.get_config">
<span class="sig-name descname"><span class="pre">get_config</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Mapping</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#pulumi_policy.StackValidationArgs.get_config" title="Permalink to this definition"></a></dt>
<dd><p>Returns configuration for the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pulumi_policy.StackValidationArgs.resources">
<span class="sig-name descname"><span class="pre">resources</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.PolicyResource" title="pulumi_policy.policy.PolicyResource"><span class="pre">PolicyResource</span></a><span class="p"><span class="pre">]</span></span></em><a class="headerlink" href="#pulumi_policy.StackValidationArgs.resources" title="Permalink to this definition"></a></dt>
<dd><p>The resources in the stack.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py" id="pulumi_policy.StackValidationPolicy">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pulumi_policy.</span></span><span class="sig-name descname"><span class="pre">StackValidationPolicy</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">validate</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><a class="reference internal" href="#pulumi_policy.StackValidationArgs" title="pulumi_policy.policy.StackValidationArgs"><span class="pre">StackValidationArgs</span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Callable</span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">Awaitable</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">enforcement_level</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.policy.EnforcementLevel"><span class="pre">EnforcementLevel</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">config_schema</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.policy.PolicyConfigSchema"><span class="pre">PolicyConfigSchema</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.StackValidationPolicy" title="Permalink to this definition"></a></dt>
<dd><p>StackValidationPolicy is a policy that validates a stack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>validate</strong> (<em>Optional</em><em>[</em><em>StackValidation</em><em>]</em>) – A callback function that validates if a stack violates a policy.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
<li><p><strong>config_schema</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.PolicyConfigSchema" title="pulumi_policy.PolicyConfigSchema"><em>PolicyConfigSchema</em></a><em>]</em>) – This policy’s configuration schema.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</section>
