---
title: Package pulumi_policy
title_tag: Package pulumi_policy | Python SDK
linktitle: pulumi_policy
notitle: true
---

<div class="section" id="module-pulumi_policy">
<span id="pulumi-policy"></span><h1>Pulumi Policy<a class="headerlink" href="#module-pulumi_policy" title="Permalink to this headline">¶</a></h1>
<p>The Pulumi Policy SDK for Python.</p>
<dl class="py class">
<dt id="pulumi_policy.EnforcementLevel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">EnforcementLevel</code><a class="headerlink" href="#pulumi_policy.EnforcementLevel" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the impact of a policy violation.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi_policy.policy.EnforcementLevel<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy function that returns true if a resource definition violates some policy (e.g., “no
public S3 buckets”), and a set of metadata useful for generating helpful messages when the policy
is violated.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_policy.Policy.name">
<code class="sig-name descname">name</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>An ID for the policy. Must be unique within the current policy set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.Policy.description">
<code class="sig-name descname">description</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of the policy rule. e.g., “S3 buckets should have default encryption
enabled.”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.Policy.enforcement_level">
<code class="sig-name descname">enforcement_level</code><em class="property">: Optional[EnforcementLevel]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.Policy.enforcement_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates what to do on policy violation, e.g., block deployment but allow override with
proper permissions.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.PolicyCustomTimeouts">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">PolicyCustomTimeouts</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">create_seconds</span><span class="p">:</span> <span class="n">float</span></em>, <em class="sig-param"><span class="n">update_seconds</span><span class="p">:</span> <span class="n">float</span></em>, <em class="sig-param"><span class="n">delete_seconds</span><span class="p">:</span> <span class="n">float</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeout options.</p>
<dl class="py attribute">
<dt id="pulumi_policy.PolicyCustomTimeouts.create_seconds">
<code class="sig-name descname">create_seconds</code><em class="property">: float</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.create_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The create resource timeout.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyCustomTimeouts.update_seconds">
<code class="sig-name descname">update_seconds</code><em class="property">: float</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.update_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The update resource timeout.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyCustomTimeouts.delete_seconds">
<code class="sig-name descname">delete_seconds</code><em class="property">: float</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyCustomTimeouts.delete_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The delete resource timeout.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.PolicyPack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">PolicyPack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">List<span class="p">[</span>Policy<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>EnforcementLevel<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyPack" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy pack contains one or more policies to enforce.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the policy pack.</p></li>
<li><p><strong>policies</strong> (<em>List</em><em>[</em><a class="reference internal" href="../pulumi_alicloud/ram/#pulumi_alicloud.ram.Policy" title="pulumi_alicloud.ram.Policy"><em>Policy</em></a><em>]</em>) – The policies associated with a policy pack.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy
violation, e.g., block deployment but allow override with
proper permissions. This is the default used for all policies in the policy pack.
Individual policies can override.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.PolicyProviderResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">PolicyProviderResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_type</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">urn</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyProviderResource" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the provider.</p>
<dl class="py attribute">
<dt id="pulumi_policy.PolicyProviderResource.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyProviderResource.props">
<code class="sig-name descname">props</code><em class="property">: Mapping[str, Any]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.props" title="Permalink to this definition">¶</a></dt>
<dd><p>The properties of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyProviderResource.urn">
<code class="sig-name descname">urn</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The URN of the provider resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyProviderResource.name">
<code class="sig-name descname">name</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyProviderResource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the provider resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.PolicyResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">PolicyResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_type</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">urn</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">pulumi_policy.policy.PolicyResourceOptions</span></em>, <em class="sig-param"><span class="n">provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi_policy.policy.PolicyProviderResource<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">parent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>PolicyResource<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">dependencies</span><span class="p">:</span> <span class="n">List<span class="p">[</span>PolicyResource<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">property_dependencies</span><span class="p">:</span> <span class="n">Dict<span class="p">[</span>str<span class="p">, </span>List<span class="p">[</span>PolicyResource<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyResource" title="Permalink to this definition">¶</a></dt>
<dd><p>PolicyResource represents a resource in the stack.</p>
<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.props">
<code class="sig-name descname">props</code><em class="property">: Mapping[str, Any]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.props" title="Permalink to this definition">¶</a></dt>
<dd><p>The outputs of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.urn">
<code class="sig-name descname">urn</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The URN of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.name">
<code class="sig-name descname">name</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.opts">
<code class="sig-name descname">opts</code><em class="property">: PolicyResourceOptions</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.opts" title="Permalink to this definition">¶</a></dt>
<dd><p>The options of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.provider">
<code class="sig-name descname">provider</code><em class="property">: Optional[PolicyProviderResource]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.parent">
<code class="sig-name descname">parent</code><em class="property">: Optional['PolicyResource']</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional parent that this resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.dependencies">
<code class="sig-name descname">dependencies</code><em class="property">: List['PolicyResource']</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.dependencies" title="Permalink to this definition">¶</a></dt>
<dd><p>The dependencies of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResource.property_dependencies">
<code class="sig-name descname">property_dependencies</code><em class="property">: Dict[str, List['PolicyResource']]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResource.property_dependencies" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of dependencies that affect each property.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.PolicyResourceOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">PolicyResourceOptions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">protect</span><span class="p">:</span> <span class="n">bool</span></em>, <em class="sig-param"><span class="n">ignore_changes</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">delete_before_replace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">aliases</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">custom_timeouts</span><span class="p">:</span> <span class="n">pulumi_policy.policy.PolicyCustomTimeouts</span></em>, <em class="sig-param"><span class="n">additional_secret_outputs</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>PolicyResourceOptions is the bag of settings that control a resource’s behavior.</p>
<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.protect">
<code class="sig-name descname">protect</code><em class="property">: bool</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.protect" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to true, protect ensures this resource cannot be deleted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.ignore_changes">
<code class="sig-name descname">ignore_changes</code><em class="property">: List[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.ignore_changes" title="Permalink to this definition">¶</a></dt>
<dd><p>Ignore changes to any of the specified properties.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.delete_before_replace">
<code class="sig-name descname">delete_before_replace</code><em class="property">: Optional[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.delete_before_replace" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to true, indicates that this resource should be deleted before
its replacement is created when replacement is necessary.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.aliases">
<code class="sig-name descname">aliases</code><em class="property">: List[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional URNs that should be aliased to this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.custom_timeouts">
<code class="sig-name descname">custom_timeouts</code><em class="property">: 'PolicyCustomTimeouts'</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.custom_timeouts" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeouts for resource create, update, and delete operations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.PolicyResourceOptions.additional_secret_outputs">
<code class="sig-name descname">additional_secret_outputs</code><em class="property">: List[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.PolicyResourceOptions.additional_secret_outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Outputs that should always be treated as secrets.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.ResourceValidationArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">ResourceValidationArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_type</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">urn</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">pulumi_policy.policy.PolicyResourceOptions</span></em>, <em class="sig-param"><span class="n">provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>PolicyProviderResource<span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>ResourceValidationArgs is the argument bag passed to a resource validation.</p>
<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.props">
<code class="sig-name descname">props</code><em class="property">: Mapping[str, Any]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.props" title="Permalink to this definition">¶</a></dt>
<dd><p>The inputs of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.urn">
<code class="sig-name descname">urn</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The URN of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.name">
<code class="sig-name descname">name</code><em class="property">: str</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.opts">
<code class="sig-name descname">opts</code><em class="property">: 'PolicyResourceOptions'</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.opts" title="Permalink to this definition">¶</a></dt>
<dd><p>The options of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_policy.ResourceValidationArgs.provider">
<code class="sig-name descname">provider</code><em class="property">: Optional['PolicyProviderResource']</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.ResourceValidationArgs.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider of the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.ResourceValidationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">ResourceValidationPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[Callable[[pulumi_policy.policy.ResourceValidationArgs, Callable[[str, Optional[str]], None]], Optional[Awaitable]], List[Callable[[pulumi_policy.policy.ResourceValidationArgs, Callable[[str, Optional[str]], None]], Optional[Awaitable]]], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi_policy.policy.EnforcementLevel<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.ResourceValidationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>ResourceValidationPolicy is a policy that validates a resource definition.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>List</strong><strong>[</strong><strong>ResourceValidation</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>validate</strong> (<em>Optional</em><em>[</em><em>Union</em><em>[</em><em>ResourceValidation</em><em>,</em>) – A callback function
that validates if a resource definition violates a policy (e.g. “S3 buckets can’t be public”).
A single callback function can be specified, or multiple functions, which are called in order.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.StackValidationArgs">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">StackValidationArgs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resources</span><span class="p">:</span> <span class="n">List<span class="p">[</span>pulumi_policy.policy.PolicyResource<span class="p">]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.StackValidationArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>StackValidationArgs is the argument bag passed to a stack validation.</p>
<dl class="py attribute">
<dt id="pulumi_policy.StackValidationArgs.resources">
<code class="sig-name descname">resources</code><em class="property">: List[PolicyResource]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_policy.StackValidationArgs.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>The resources in the stack.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_policy.StackValidationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_policy.</code><code class="sig-name descname">StackValidationPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Optional[Callable[[pulumi_policy.policy.StackValidationArgs, Callable[[str, Optional[str]], None]], Optional[Awaitable]]]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi_policy.policy.EnforcementLevel<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_policy.StackValidationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>StackValidationPolicy is a policy that validates a stack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – An ID for the policy. Must be unique within the current policy set.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A brief description of the policy rule. e.g., “S3 buckets should have
default encryptionenabled.”</p></li>
<li><p><strong>validate</strong> (<em>Optional</em><em>[</em><em>StackValidation</em><em>]</em>) – A callback function that validates if a stack violates a policy.</p></li>
<li><p><strong>enforcement_level</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_policy.EnforcementLevel" title="pulumi_policy.EnforcementLevel"><em>EnforcementLevel</em></a><em>]</em>) – Indicates what to do on policy violation,
e.g., block deployment but allow override with proper permissions.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
